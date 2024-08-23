yum install snapd
systemctl enable --now snapd.socket
ln -s /var/lib/snapd/snap /snap
sleep(5)
snap install deno
exec /bin/bash