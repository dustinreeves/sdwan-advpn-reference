from ansible_collections.ansible.utils.plugins.filter.ipaddr import ipaddr


class FilterModule(object):
    def filters(self):
        return {"ipaddr": ipaddr}
