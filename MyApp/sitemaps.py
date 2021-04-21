from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['sd_series', 'mr_series', 'arm_series', 'elec_series', 'fluids_l', 'paste', 'fluids_p', 'dev', 'test', 'prod', 'admin_login', 'admin_login/stats']

    def location(self, item):
        return reverse(item)