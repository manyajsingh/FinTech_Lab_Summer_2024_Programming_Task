from sec_edgar_downloader import Downloader
dl = Downloader("Manya", "manya105btcseai23@igdtuw.ac.in")

dl.get("10-K", "AAPL", after='1995-01-01', before='2023-12-31')
dl.get("10-K", "MSFT", after='1995-01-01', before='2023-12-31')
dl.get("10-K", "V", after='1995-01-01', before='2023-12-31')