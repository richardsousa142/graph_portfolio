import utils.config as config_session
import utils.cols as cols_b3
import utils.width as width
import pandas as pd
import io
import os
import logging
 
logger = logging.getLogger(__name__)

class B3PublicData:
    BASE_URL = "https://bvmf.bmfbovespa.com.br/InstDados/SerHist/"
    
    def __init__(self, url: str = None):
        self.url = url or self.BASE_URL
        self.session = None

    def read_df_year(self, year: int) -> pd.DataFrame:
        file_name = f"COTAHIST_A{year}.ZIP"
        url = self.url + file_name

        raw_data = self._get_info(url)

        df = pd.read_fwf(
            io.BytesIO(raw_data),
            skiprows=1,
            compression="zip",
            names=cols_b3.COLS,
            widths=width.WIDTH,
        )

        # Remove a última linha (rodapé)
        if not df.empty:
            df = df.iloc[:-1]

        return df

    def _get_info(self, url: str) -> bytes:
        ses = self._session()

        print(f"Obtendo informações diretamente da B3")
        r = ses.get(url, timeout=60, allow_redirects=True)

        if r.status_code == 404:
            logger.info("Arquivo B3 não encontrado (404): %s", url)
            raise FileNotFoundError(url)

        r.raise_for_status()
        return r.content

    def _session(self):
        # singleton para criar o session
        if self.session is None:
            self.session = config_session.session()
        return self.session