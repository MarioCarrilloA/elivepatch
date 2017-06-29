#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2017, Alice Ferrazzi <alice.ferrazzi@gmail.com>
# Distributed under the terms of the GNU General Public License v2 or later

import subprocess
import os

class PaTch(object):

    def __init__(self):
        self.config_file = None
        self.patch_file = None
        self.kernel_version = None
        self.livepatch_status = "Not started"
        self.kernel_dir = None

    def set_kernel_dir(self, kernel_dir):
        self.kernel_dir = kernel_dir

    def get_kernel_dir(self):
        return self.kernel_dir

    def set_lp_status(self, livepatch_status):
        self.livepatch_status = livepatch_status

    def get_lp_status(self):
        return self.livepatch_status

    def update_lp_status(self, file):
        if os.path.isfile(file):
            self.livepatch_status = 'done'
        return self.livepatch_status

    def set_kernel_version(self, kernel_version):
        self.kernel_version = kernel_version

    def get_kernel_version(self):
        return self.kernel_version

    def get_config(self):
        return self.config_file

    def set_config(self, config_file):
        self.config_file = config_file

    def set_patch(self, patch_file):
        self.patch_file = patch_file

    def get_patch(self):
        return self.patch_file

    def kernel_version(self):
        pass

    def compare_kernel_config(self):
        pass

    def recompile_kernel(self):
        pass

    def search_kernel_source_path(self):
        pass

    def get_kernel_source_path(self):
        self.kernel_path =''
        return self.kernel_path

    # kpatch-build/kpatch-build -s /usr/src/linux-4.9.16-gentoo/
    # -v /usr/src/linux-4.9.16-gentoo/vmlinux examples/test.patch
    # -c ../elivepatch/elivepatch_server/config --skip-gcc-check
    def build_livepatch(self, kernel_source, vmlinux):
        """
        
        :param kernel_source: 
        :param vmlinux: 
        :return: 
        """
        bashCommand = 'sudo kpatch-build'
        bashCommand += ' -s '+ kernel_source
        bashCommand += ' -v '+ vmlinux
        bashCommand += ' -c '+ self.config_file
        bashCommand += ' ' + self.patch_file
        bashCommand += ' --skip-gcc-check'
        print(bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
