from threading import Thread, Lock
from urllib.request import urlopen, Request, URLError


class FetchUrls(Thread):

    """
    Threading checking URLs.
    """

    def __init__(self, urls, output, lock):

        """
        Constructor
        @param urls list of urls to check
        @param output file to write urls output
        """
        Thread.__init__(self)
        self.lock = lock
        self.urls = urls
        self.output = output

    def run(self):

        while self.urls:
            self.lock.acquire()
            d = None
            a = list()
            url = self.urls.pop()
            req = Request(url)
            try:
                d = urlopen(req)
                a.append(d)
            except URLError as e:
                print('URL {1} failed: {0}'.format(url, e.reason))
            dreq = a.pop()
            self.output.write(str(dreq.read))
            print('URL {1} fetched by {0}'.format(url, self.name))
            self.lock.release()


def main():
    urls1 = ['http://www.google.com', 'http://www.facebook.com']
    urls2 = ['http://www.yahoo.com', 'http://www.youtube.com']
    f = open('output.txt', 'w+')
    t1 = FetchUrls(urls1, f, Lock())
    t2 = FetchUrls(urls2, f, Lock())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()


if __name__ == '__main__':
    main()
