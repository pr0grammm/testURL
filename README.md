# testURL
python tool to process URL's and check whether they can be accessed or not

The tool reads URL's from a file - "urlfile" and sends a head request to every URL read.
If an HTTP response is received and status code begins with a 2 we write success ([+]).
If no HTTP response is received or status code does not begin with 2 we write failure([-]).

Usage: python testURL.py urlfile

