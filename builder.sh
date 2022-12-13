yum-builddep  rpmbuild/SPECS/openresty.spec -y
rpmbuild -ba rpmbuild/SPECS/openresty.spec
rpm -i  rpmbuild/RPMS/x86_64/openresty-1.19.9.1-0.x86_64.rpm

