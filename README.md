# zoning-archive-server

**Note: this is a demo, not production code.** This is the back-end component of a potential replacement for the Zoning Archive, a public-facing search portal for zoning-, development-, and permit-related documents from L&I. This is intended as a temporary workaround for issues in the current system.

## Installation

1. `git clone` this repo.
2. Install requirements with `pip install -f requirements.txt`, ideally to a [`virtualenv`](https://virtualenv.pypa.io/en/latest/). If on Windows,  use `requirements-win.txt`, then download a pre-built version `cx_Oracle` from [this page](http://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_oracle). Make sure it matches the version of Python and bits of the system you're on. Install that file with `pip install C:\path\to\cx_Oracle-5.2.1+oci12c-cpXX-none-winXX.whl`.
3. Copy `config_sample.py` and rename it to `config.py`. Specify actual values for connecting to the Oracle database and querying the Zoning Archive view.

## Usage

Run the application with `python app.py`. By default it will run on port 8080. To change that, edit the line `app.run(host='0.0.0.0', port=XXXX, debug=True)`.

## API

The API consists of a single endpoint `/address/<address>/documents/`, which returns a list of documents and necessary attributes for forming image URLs.

    {
      inputAddress: "1234 MARKET ST",
      documents: [
        {
          addressId: "1234 MARKET ST",
          appDocId: 235748,
          appId: "219",
          docId: "219|235748",
          docType: "FILES",
          numPages: 617,
          scanDate: "2009-01-05"
        },
        ...
      ]
    }
The URL to view a single page is then constructed as `http://www.phila.gov/zoningarchive/GenerateImage.aspx?app=<appId>&docID=<appDocId>&pageNum=<page>`.
