#!/usr/bin/python3
import ansible.module_utils.basic as an
import requests as r

def main():

    fields = {"webpage": {"default": "https://example.com", "type": "str"}}

    module = an.AnsibleModule(argument_spec=fields)
    code = r.head(module.params['webpage']).status_code
    module.exit_json(meta={'webpage': module.params['webpage'], 'status_code': code})

if __name__ == '__main__':
    main()