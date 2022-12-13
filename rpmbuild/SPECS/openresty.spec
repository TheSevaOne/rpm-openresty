Name:           openresty
Version:        1.19.9.1
Release:        0
Summary:        Scalable Web Platform by Extending NGINX with Lua.
Group:          Productivity/Networking/Web/Servers
License:        BSD
URL:            https://openresty.org
Source:         https://openresty.org/download/%{name}-%{version}.tar.gz
Prefix:         %{_prefix}
Packager: 	Averkov Vsevolod 
BuildRoot:      %{_tmppath}/%{name}-root
BuildArch:	x86_64
BuildRequires:	sed openssl-devel pcre-devel readline-devel  GeoIP-devel gcc perl(Data::Dumper) perl(Digest::MD5) 
Requires:	openssl pcre readline 
Source1:        	openresty.init
%description
Scalable Web Platform by Extending NGINX with Lua.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure   --with-ipv6 --with-pcre-jit --with-http_geoip_module --with-http_stub_status_module --with-http_realip_module --with-http_v2_module --with-http_slice_module
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/etc/init.d
%{__install} -p -m 0755 %{SOURCE1} %{buildroot}/etc/init.d/%{name}
%clean
rm -rf %{buildroot}

%post
%systemd_post openresty.service

%postun
%systemd_postun_with_restart openresty.service


%files
%define user_dir /usr/local/openresty
%defattr(-,root,root,-)
%attr(755,root,root) /etc/init.d/openresty
  %{user_dir}/COPYRIGHT
   %{user_dir}/bin/md2pod.pl
   %{user_dir}/bin/nginx-xml2pod
   %{user_dir}/bin/openresty
   %{user_dir}/bin/opm
   %{user_dir}/bin/resty
   %{user_dir}/bin/restydoc
   %{user_dir}/bin/restydoc-index
   %{user_dir}/luajit/*
   %{user_dir}/lualib/*
   %{user_dir}/nginx/*
   %{user_dir}/pod/*
   %{user_dir}/resty.index

  




