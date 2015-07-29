Summary: Program that wraps normal socket connections with SSL/TLS
Name: stunnel
Version: 4.08
Release: 1
Copyright: GPL
Group: Applications/Networking
Source: stunnel-%{version}.tar.gz
Packager: neeo <neeo@irc.pl>
Requires: openssl >= 0.9.6g
Buildroot: /var/tmp/stunnel-%{version}-root

%description
The stunnel program is designed to work as SSL encryption wrapper
between remote clients and local (inetd-startable) or remote
servers. The concept is that having non-SSL aware daemons running on
your system you can easily set them up to communicate with clients over
secure SSL channels.
stunnel can be used to add SSL functionality to commonly used inetd
daemons like POP-2, POP-3, and IMAP servers, to standalone daemons like
NNTP, SMTP and HTTP, and in tunneling PPP over network sockets without
changes to the source code.
 
%prep
%setup -n stunnel-%{version}


%build
if [ ! -x ./configure ]; then
    autoconf
    autoheader
fi

CFLAGS="${RPM_OPT_FLAGS}" ./configure --prefix=/usr --sysconfdir=/etc --with-tcp-wrappers

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/stunnel
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/usr/man/man8

install -m755 -s src/stunnel $RPM_BUILD_ROOT/usr/sbin
install -m755 -s src/.libs/libstunnel.so $RPM_BUILD_ROOT/usr/lib
install -m755 -s src/.libs/libstunnel.la $RPM_BUILD_ROOT/usr/lib
install -m644 doc/stunnel.8 $RPM_BUILD_ROOT/usr/man/man8
install -m644 tools/stunnel.conf-sample $RPM_BUILD_ROOT/etc/stunnel

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root)
%doc doc/stunnel.html doc/en/transproxy.txt doc/en/VNC_StunnelHOWTO.html
%doc tools/ca.html tools/ca.pl tools/importCA.html tools/importCA.sh tools/stunnel.cnf
/etc/stunnel/stunnel.conf-sample
/usr/sbin/stunnel
/usr/lib/libstunnel.so
/usr/lib/libstunnel.la
/usr/man/man8/stunnel.8.gz

%changelog
* Wed Mar 17 2004 neeo <neeo@irc.pl>
- updated for 4.05

* Sun Jun 24 2000 Brian Hatch <bri@stunnel.org>
- updated for 3.8p3

* Wed Jul 14 1999 Dirk O. Siebnich <dok@vossnet.de>
- updated for 3.5.

* Mon Jun 07 1999 Dirk O. Siebnich <dok@vossnet.de>
- adapted from sslwrap RPM spec file
