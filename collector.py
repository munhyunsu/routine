class Collector(object):
    """Collector
    provide interface for child collector
    """
    def do_collect(self):
        raise NotImplemented

