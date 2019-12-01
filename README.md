# emails-from-pdfs

>Extract email addresses from PDFs stored in multiple folders.

Script runs through all folders, subfolders and files in given location and extracts email addresses from 1st pages.

![](https://i.ibb.co/KLyVzzS/Whats-App-Image-2019-11-29-at-14-06-55.jpg)

## How to use

1) Prepare your PDFs - put them in folders.
2) Put main folder location in `rootdir` variable.
3) By default script takes first page of a PDF (`pageObj = pdfReader.getPage(0)`) and there it looks for email address.
4) Modify regex if needed in `re.search("", full_text)`. By modyfing regex you can easily adapt this script to look for phone numbers, addresses and other info.

## Roadmap

- Try different pdf-reading libraries to improve success rate.

## Release History

- 0.1: Launch.

## Versioning

Using [SemVer](http://semver.org/).

## License

GNU General Public License v3.0, see [LICENSE.md](https://github.com/vardecab/emails-from-pdfs/blob/master/LICENSE).

## Acknowledgements

- [PyPDF2](https://pypi.org/project/PyPDF2/)