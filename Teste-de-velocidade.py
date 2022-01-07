import speedtest

test = speedtest.Speedtest()
test.get_best_server()

down = test.download()
rsDown = round(down)
fdown = int(rsDown / 1e+6)

upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)


print (f"DOWNLOAD: {fdown} mb/s")
print(f"UPLOAD: {fUp} mb/s")