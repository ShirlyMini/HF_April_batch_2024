pytest -v -s -m "regression" --html=Reports\regression_egde.html --browser edge
rem pytest -v -s -m "regression" --html=Reports\regression_ff.html --browser firefox
rem pytest -v -s -m "sanity" --html=Reports\sanity_chrome.html --browser chrome