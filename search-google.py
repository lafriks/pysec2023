from googlesearch import search
res = search(
    "index inurl:ftp -inurl:(http|https)",
    advanced=True
)

print('FTP sites:')
for r in res:
    print('%s' % r.url)
