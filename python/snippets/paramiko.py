#!/bin/python3

# examples
# https://www.programcreek.com/python/example/4561/paramiko.SSHClient
# https://linuxhint.com/paramiko-python/

def _ssh_run_remote_command(self, cmd):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=self.host,
                           username=self.config['ssh_user'],
                           password=self.config['ssh_password'])
        stdin, stdout, stderr = ssh_client.exec_command(cmd)

        out = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        if self.log_level:
            logger.info(out)
        if error:
            raise Exception('There was an error pulling the runtime: {}'.format(error))
        ssh_client.close()
        return out 

def ssh_edit_file(adress, user, passw, remotefile, regex, replace):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        trans = paramiko.Transport((adress, 22))
        trans.connect(username=user, password=passw)
        sftp = paramiko.SFTPClient.from_transport(trans)
        f_in = sftp.file(remotefile, "r")
        c_in = f_in.read()
        pattern = re.compile(regex, re.MULTILINE | re.DOTALL)
        c_out = pattern.sub(replace, c_in)
        f_out = sftp.file(remotefile, "w")
        f_out.write(c_out)
        f_in.close()
        f_out.close()
        sftp.close()
        trans.close() 

def fetch_remote_crashes(self):
        """
        some exception handling code is taken from https://www.programcreek.com/python/example/105570/scp.SCPClient
        """
        try:
            ssh = SSHClient()
            ssh.load_system_host_keys()
            ssh.connect(hostname=config.remote_system_ip)
            self.copy_crashes_dir_with_scp(ssh)
        except AuthenticationException:
            print("Authentication failed, please verify your credentials: %s")
        except SSHException as sshException:
            print("Unable to establish SSH connection: %s" % sshException)
        except BadHostKeyException as badHostKeyException:
            print("Unable to verify server's host key: %s" % badHostKeyException)
        finally:
            ssh.close() 

