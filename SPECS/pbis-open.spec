Name: 		pbis-open
Summary: 	Identity Services for authenticating with Active Directory domains
Version: 	8.2.3
Release: 	1.7.7
License: 	GPLv2
URL:	http://www.beyondtrust.com/Products/PowerBroker-Identity-Services-Open-Edition/

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/pbis-open/archive?at=f511d332d41&format=tar.gz&prefix=pbis-open-8.2.3#/pbis-open-8.2.3.tar.gz

Patch0: CA-281555-PBIS-in-XS7.1-loses-group-memberships.patch
Patch1: CA-291988-Ignore-unknown-krb5.conf-directives.patch
Patch2: build-makefiles.patch
Patch3: Disable-AM_C_PROTOTYPES-which-is-for-old-automake.patch
Patch4: resolve-gcc-4.8-error-unused-local-typedefs.patch
Patch5: Fix-rm-libtoolT-error.patch
Patch6: pbis-fix-krb5.patch
Patch7: pbis-fix-libxml2.patch
Patch8: pbis-fix-for-libxml2-autotools.patch
Patch9: pbis-fix-lsass.patch
Patch10: CP-13276-Simplify-PBIS8-build-and-decouple-the-PBIS-.patch
Patch11: nss-remap-uid-to-root.patch
Patch12: CP-12576-Integrate-automatic-upgrade-tool-from-Likew.patch
Patch13: CP-12576-Do-symbol-link-for-pam_lsass.so.patch
Patch14: CA-206905-PBIS-service-started-when-it-shouldn-t-be.patch
Patch15: CA-208359-PBIS-services-should-start-on-demand-in-do.patch
Patch16: CA-209500-pbis-systemd-log-spam-on-every-boot.patch
Patch17: CA-249223-XenCenter-fails-to-login-members-of-a-AD-g.patch
Patch18: CA-214745-Change-lwsmd.service-from-0755-to-0644.patch
Patch19: upgrade-likewise-to-pbis.patch
Patch20: CA-324607-Do-not-add-capath-entries-for-SLD-54456.patch
Patch21: CA-338602-lwsmd-daemon-should-not-be-running-when-AD-is-not-configured

Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/pbis.pg/archive?at=v1.7.7&format=tar#/pbis.patches.tar) = e354e19eb1412eeac8618f582942a14d6f23c13e

Requires: grep, sh-utils, pbis-open-upgrade, libcurl
Conflicts:  winbind 
Obsoletes: likewise-open, likewise-base, likewise-domainjoin, likewise-domainjoin-gui, likewise-eventlog, likewise-krb5, likewise-libxml2, likewise-lsass, likewise-lwconfig, likewise-lwio, likewise-lwreg, likewise-lwreskit, likewise-lwtools, likewise-lwupgrade, likewise-mod-auth-kerb, likewise-netlogon, likewise-openldap, likewise-passwd, likewise-pstore, likewise-rpc, likewise-sqlite, likewise-srvsvc
BuildRequires: gcc, glibc-devel, pam-devel, ncurses-devel, flex, bison, rpm-build, rpm-devel, popt-devel, libxml2-devel, autoconf, automake, libtool, libuuid-devel, libedit-devel, openssl-devel, libcurl-devel, doxygen
BuildRequires: systemd-devel
%{?systemd_requires}
Provides: likewise-open
Provides: xenserver-active-directory
AutoReq:no
AutoProv:no

%description
PowerBroker Identity Services Open integrates Unix desktops and servers into an Active Directory environment by joining hosts to the domain and lets Unix applications and services authenticate MS Windows' users and groups via the PAM and Name Service Switch libraries.

%package devel
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/pbis.pg/archive?at=v1.7.7&format=tar#/pbis.patches.tar) = e354e19eb1412eeac8618f582942a14d6f23c13e
Summary: PowerBroker Identity Services Open (development)
Requires: pbis-open


%description devel
The pbis-open-devel package includes the development libraries and header files that supply the application programming interface for security and authentication.

%prep
%autosetup -v -p1

%build
mkdir -p transformerbuild
cd transformerbuild
../configure --oem=oem18 --host-arch=x86_64 --build-isas=x86_64 --build-arch=x86_64 --build-multiarch=none --build-id=%{release} --package-rpm=no ../build/mk-config/linux-x86_64-rpm.conf
make -j4 all

%install
mkdir -p %{buildroot}/var/lib/pbis/rpc
for FILE in /opt/pbis/bin/kinit \
		/opt/pbis/bin/klist \
		/opt/pbis/bin/kdestroy \
		/opt/pbis/bin/kvno \
		/opt/pbis/bin/ktutil \
		/opt/pbis/lib/krb5/plugins/preauth/pkinit.so \
		/opt/pbis/lib/libcom_err.so.3.0 \
		/opt/pbis/lib/libcom_err.so.3 \
		/opt/pbis/lib/libk5crypto.so.3.1 \
		/opt/pbis/lib/libk5crypto.so.3 \
		/opt/pbis/lib/libgssapi_krb5.so.2.2 \
		/opt/pbis/lib/libgssapi_krb5.so.2 \
		/opt/pbis/lib/libkrb5.so.3.3 \
		/opt/pbis/lib/libkrb5.so.3 \
		/opt/pbis/lib/libkadm5srv_mit.so.8.0 \
		/opt/pbis/lib/libkadm5srv_mit.so.8 \
		/opt/pbis/lib/libkdb5.so.5.0 \
		/opt/pbis/lib/libkdb5.so.5 \
		/opt/pbis/lib/libgssrpc.so.4.1 \
		/opt/pbis/lib/libgssrpc.so.4 \
		/opt/pbis/lib/libkrb5support.so.0.1 \
		/opt/pbis/lib/libkrb5support.so.0 \
		/opt/pbis/lib/sasl2/libgssapiv2.so.2.0.23 \
		/opt/pbis/lib/sasl2/libgssapiv2.so.2 \
		/opt/pbis/lib/sasl2/libgssapiv2.so \
		/opt/pbis/lib/sasl2/libgssspnego.so.2.0.23 \
		/opt/pbis/lib/sasl2/libgssspnego.so.2 \
		/opt/pbis/lib/sasl2/libgssspnego.so \
		/opt/pbis/lib/libsasl2.so.2.0.23 \
		/opt/pbis/lib/libsasl2.so.2 \
		/opt/pbis/lib/libldap-2.4.so.2.4.2 \
		/opt/pbis/lib/libldap-2.4.so.2 \
		/opt/pbis/lib/liblber-2.4.so.2.4.2 \
		/opt/pbis/lib/liblber-2.4.so.2 \
		/opt/pbis/lib/libldap_r-2.4.so.2.4.2 \
		/opt/pbis/lib/libldap_r-2.4.so.2 \
		/opt/pbis/bin/ldapsearch \
		/opt/pbis/bin/sqlite3 \
		/opt/pbis/lib/libsqlite3.so.0.8.6 \
		/opt/pbis/lib/libsqlite3.so.0 \
		/opt/pbis/lib/libtdb.so.0.0.0 \
		/opt/pbis/lib/libtdb.so.0 \
		/opt/pbis/lib/liblwbase_nothr.so.0.0.0 \
		/opt/pbis/lib/liblwbase_nothr.so.0 \
		/opt/pbis/lib/liblwbase.so.0.0.0 \
		/opt/pbis/lib/liblwbase.so.0 \
		/opt/pbis/sbin/lw-svcm-wrap \
		/opt/pbis/docs/html/lwbase \
		/opt/pbis/lib/liblwmsg_nothr.so.0.0.0 \
		/opt/pbis/lib/liblwmsg_nothr.so.0 \
		/opt/pbis/lib/liblwmsg.so.0.0.0 \
		/opt/pbis/lib/liblwmsg.so.0 \
		/opt/pbis/libexec/lwma \
		/opt/pbis/docs/html/lwmsg \
		/opt/pbis/lib/libregcommon.so.0.0.0 \
		/opt/pbis/lib/libregcommon.so.0 \
		/opt/pbis/lib/libregclient.so.0.0.0 \
		/opt/pbis/lib/libregclient.so.0 \
		/opt/pbis/lib/librsutils.so.0.0.0 \
		/opt/pbis/lib/librsutils.so.0 \
		/opt/pbis/lib/lw-svcm/lwreg-sqlite.so \
		/opt/pbis/lib/lw-svcm/lwreg-memory.so \
		/opt/pbis/lib/lw-svcm/lwreg.so \
		/opt/pbis/share/config/lwreg.reg \
		/opt/pbis/bin/regshell \
		/opt/pbis/bin/edit-reg \
		/opt/pbis/lib/liblwadvapi.so.0.0.0 \
		/opt/pbis/lib/liblwadvapi.so.0 \
		/opt/pbis/lib/liblwadvapi_nothr.so.0.0.0 \
		/opt/pbis/lib/liblwadvapi_nothr.so.0 \
		/opt/pbis/lib/liblwnetcommon.so.0.0.0 \
		/opt/pbis/lib/liblwnetcommon.so.0 \
		/opt/pbis/lib/liblwnetclientapi.so.0.0.0 \
		/opt/pbis/lib/liblwnetclientapi.so.0 \
		/opt/pbis/lib/lw-svcm/netlogon.so \
		/opt/pbis/lib/krb5/plugins/libkrb5/liblwnet_service_locator.so \
		/opt/pbis/bin/get-dc-name \
		/opt/pbis/bin/get-dc-list \
		/opt/pbis/bin/get-dc-time \
		/opt/pbis/share/config/netlogond.reg \
		/opt/pbis/lib/liblwiocommon.so.0.0.0 \
		/opt/pbis/lib/liblwiocommon.so.0 \
		/opt/pbis/lib/liblwioshareinfo.so.0.0.0 \
		/opt/pbis/lib/liblwioshareinfo.so.0 \
		/opt/pbis/lib/liblwioclient.so.0.0.0 \
		/opt/pbis/lib/liblwioclient.so.0 \
		/opt/pbis/lib/libiomgr.so.0.0.0 \
		/opt/pbis/lib/libiomgr.so.0 \
		/opt/pbis/lib/liblwiosmbcommon.so.0.0.0 \
		/opt/pbis/lib/liblwiosmbcommon.so.0 \
		/opt/pbis/lib/lwio-driver/rdr.so \
		/opt/pbis/lib/lw-svcm/lwio.so \
		/opt/pbis/lib/libiotest.sys.so \
		/opt/pbis/bin/lwio-driver \
		/opt/pbis/bin/lwio-copy \
		/opt/pbis/share/config/lwiod.reg \
		/opt/pbis/share/config/rdr.reg \
		/opt/pbis/lib/libschannel.so.0.0.0 \
		/opt/pbis/lib/libschannel.so.0 \
		/opt/pbis/lib/libdcerpc.so.1.2.0 \
		/opt/pbis/lib/libdcerpc.so.1 \
		/opt/pbis/lib/lw-svcm/dcerpc.so \
		/opt/pbis/share/config/dcerpcd.reg \
		/opt/pbis/lib/libcentutils.so.0.0.0 \
		/opt/pbis/lib/libcentutils.so.0 \
		/opt/pbis/lib/liblwsmcommon.so.0.0.0 \
		/opt/pbis/lib/liblwsmcommon.so.0 \
		/opt/pbis/lib/liblwsm.so.0.0.0 \
		/opt/pbis/lib/liblwsm.so.0 \
		/opt/pbis/bin/lwsm \
		/opt/pbis/sbin/lwsmd \
		/opt/pbis/docs/html/lwsm \
		/opt/pbis/lib/libadtool.so.0.0.0 \
		/opt/pbis/lib/libadtool.so.0 \
		/opt/pbis/bin/adtool \
		/opt/pbis/lib/libeventlogutils.so.0.0.0 \
		/opt/pbis/lib/libeventlogutils.so.0 \
		/opt/pbis/lib/libeventlog.so.0.0.0 \
		/opt/pbis/lib/libeventlog.so.0 \
		/opt/pbis/lib/libeventlog_norpc.so.0.0.0 \
		/opt/pbis/lib/libeventlog_norpc.so.0 \
		/opt/pbis/lib/lw-svcm/eventlog.so \
		/opt/pbis/bin/eventlog-cli \
		/opt/pbis/share/config/eventlogd.reg \
		/opt/pbis/lib/liblsacommon.so.0.0.0 \
		/opt/pbis/lib/liblsacommon.so.0 \
		/opt/pbis/lib/liblsapstore.so.0.0.0 \
		/opt/pbis/lib/liblsapstore.so.0 \
		/opt/pbis/lib/liblsaclient.so.0.0.0 \
		/opt/pbis/lib/liblsaclient.so.0 \
		/opt/pbis/lib/liblsaclientthr.so.0.0.0 \
		/opt/pbis/lib/liblsaclientthr.so.0 \
		/opt/pbis/lib/liblsaclient_ntlm.so.0.0.0 \
		/opt/pbis/lib/liblsaclient_ntlm.so.0 \
		/opt/pbis/lib/liblsarpc.so.0.0.0 \
		/opt/pbis/lib/liblsarpc.so.0 \
		/opt/pbis/lib/liblsaauth.so.0.0.0 \
		/opt/pbis/lib/liblsaauth.so.0 \
		/opt/pbis/lib/lw-map-sec/lsass.so \
		/opt/pbis/lib/gss/libgssapi_ntlm.so \
		/opt/pbis/lib/liblsagsswrap.so.0.0.0 \
		/opt/pbis/lib/liblsagsswrap.so.0 \
		/opt/pbis/lib/liblsaserverapi.so.0.0.0 \
		/opt/pbis/lib/liblsaserverapi.so.0 \
		/opt/pbis/lib/libntlmserver.so.0.0.0 \
		/opt/pbis/lib/libntlmserver.so.0 \
		/opt/pbis/lib/libdsapi.so.0.0.0 \
		/opt/pbis/lib/libdsapi.so.0 \
		/opt/pbis/lib/lsa-provider/local.so \
		/opt/pbis/lib/lsa-provider/ad_open.so \
		/opt/pbis/lib/lsa-rpc/samr.so \
		/opt/pbis/lib/lsa-rpc/lsa.so \
		/opt/pbis/lib/lsa-rpc/dssetup.so \
		/opt/pbis/lib/lsa-rpc/wkssvc.so \
		/opt/pbis/lib/lw-svcm/lsass.so \
		/opt/pbis/bin/lsa \
		/opt/pbis/bin/ad-cache \
		/opt/pbis/bin/add-group \
		/opt/pbis/bin/add-user \
		/opt/pbis/bin/del-group \
		/opt/pbis/bin/del-user \
		/opt/pbis/bin/enum-groups \
		/opt/pbis/bin/enum-users \
		/opt/pbis/bin/find-by-sid \
		/opt/pbis/bin/find-group-by-id \
		/opt/pbis/bin/find-group-by-name \
		/opt/pbis/bin/find-user-by-id \
		/opt/pbis/bin/find-user-by-name \
		/opt/pbis/bin/get-metrics \
		/opt/pbis/bin/get-status \
		/opt/pbis/bin/pbis-status \
		/opt/pbis/bin/list-groups-for-user \
		/opt/pbis/bin/ypcat \
		/opt/pbis/bin/ypmatch \
		/opt/pbis/bin/mod-group \
		/opt/pbis/bin/mod-user \
		/opt/pbis/bin/find-objects \
		/opt/pbis/bin/enum-objects \
		/opt/pbis/bin/enum-members \
		/opt/pbis/bin/query-member-of \
		/opt/pbis/bin/passwd \
		/opt/pbis/share/config/lsassd.reg \
		/opt/pbis/share/config/privileges.reg \
		/opt/pbis/share/config/accounts.reg \
		/opt/pbis/docs/html/lsass \
		/opt/pbis/lib/liblwdns.so.0.0.0 \
		/opt/pbis/lib/liblwdns.so.0 \
		/opt/pbis/bin/update-dns \
		/opt/pbis/lib/liblwnetapi.so.0.0.0 \
		/opt/pbis/lib/liblwnetapi.so.0 \
		/opt/pbis/lib/libOpenSOAPClient.so.2.0.0 \
		/opt/pbis/lib/libOpenSOAPClient.so.2 \
		/opt/pbis/lib/libOpenSOAPSecurity.so.2.0.0 \
		/opt/pbis/lib/libOpenSOAPSecurity.so.2 \
		/opt/pbis/lib/libOpenSOAPService.so.2.0.0 \
		/opt/pbis/lib/libOpenSOAPService.so.2 \
		/opt/pbis/lib/libdomainjoin.so.0.0.0 \
		/opt/pbis/lib/libdomainjoin.so.0 \
		/opt/pbis/bin/domainjoin-cli \
		/opt/pbis/libexec/ConfigureLogin \
		/opt/pbis/libexec/gpcron \
		/opt/pbis/bin/config \
		/opt/pbis/libexec/conf2reg \
		/opt/pbis/libexec/regupgr61.sh \
		/opt/pbis/libexec/reg61sed.sh \
		/opt/pbis/lib/libwbclient.so.0.0.0 \
		/opt/pbis/lib/libwbclient.so.0 \
		/opt/pbis/lib/lwicompat_v4.so \
		/opt/pbis/lib/lw-pstore/samba.so \
		/opt/pbis/bin/samba-interop-install \
		/opt/pbis/libexec/init-base.sh \
		/opt/pbis/data/VERSION \
		/opt/pbis/bin/uninstall.sh \
		/opt/pbis/share/pbis.pam-auth-update \
		/opt/pbis/share/rhel/7.0/pbis.te \
		/opt/pbis/share/rhel/7.0/pbis.fc \
		/opt/pbis/share/rhel/7.0/pbis.if \
		/opt/pbis/share/rhel/7.0/pbis.pp \
		/opt/pbis/share/rhel/6.0/pbis.te \
		/opt/pbis/share/rhel/6.0/pbis.fc \
		/opt/pbis/share/rhel/6.0/pbis.if \
		/opt/pbis/share/rhel/6.0/pbis.pp \
		/opt/pbis/share/fedora/20/pbis.te \
		/opt/pbis/share/fedora/20/pbis.fc \
		/opt/pbis/share/fedora/20/pbis.if \
		/opt/pbis/share/fedora/20/pbis.pp \
		/opt/pbis/share/fedora/19/pbis.te \
		/opt/pbis/share/fedora/19/pbis.fc \
		/opt/pbis/share/fedora/19/pbis.if \
		/opt/pbis/share/fedora/19/pbis.pp \
		/opt/pbis/share/fedora/18/pbis.te \
		/opt/pbis/share/fedora/18/pbis.fc \
		/opt/pbis/share/fedora/18/pbis.if \
		/opt/pbis/share/fedora/18/pbis.pp \
		/opt/pbis/share/fedora/17/pbis.te \
		/opt/pbis/share/fedora/17/pbis.fc \
		/opt/pbis/share/fedora/17/pbis.if \
		/opt/pbis/share/fedora/17/pbis.pp \
		/opt/pbis/share/fedora/16/pbis.te \
		/opt/pbis/share/fedora/16/pbis.fc \
		/opt/pbis/share/fedora/16/pbis.if \
		/opt/pbis/share/fedora/16/pbis.pp \
		/opt/pbis/share/fedora/15/pbis.te \
		/opt/pbis/share/fedora/15/pbis.fc \
		/opt/pbis/share/fedora/15/pbis.if \
		/opt/pbis/share/fedora/15/pbis.pp \
		/opt/pbis/share/fedora/14/pbis.te \
		/opt/pbis/share/fedora/14/pbis.fc \
		/opt/pbis/share/fedora/14/pbis.if \
		/opt/pbis/share/fedora/14/pbis.pp \
		/opt/pbis/share/fedora/13/pbis.te \
		/opt/pbis/share/fedora/13/pbis.fc \
		/opt/pbis/share/fedora/13/pbis.if \
		/opt/pbis/share/fedora/13/pbis.pp \
		/opt/pbis/libexec/pbis-support.pl \
		/opt/pbis/docs/pbis-open-installation-and-administration-guide.pdf \
		/opt/pbis/docs/pbis-quick-start-guide-for-linux.pdf \
		/opt/pbis/lib/krb5/plugins/preauth/pacreq.so \
		/lib/security/pam_lsass.so \
		/lib/security/pam_lsass.la \
		/lib/libnss_lsass.so.2 \
		/lib/libnss_lsass.la \
		/usr/bin/pbis \
		/usr/bin/domainjoin-cli \
		/etc/pbis/pbis-krb5-ad.conf \
		/var/lib/pbis/lwreport.xml \
		/etc/pbis/gss/mech \
		/etc/pbis/user-ignore \
		/etc/pbis/group-ignore \
		/var/lib/pbis/lwconfig.xml \
		/etc/pbis/debian/lwsmd \
		/etc/pbis/redhat/lwsmd \
		/etc/pbis/redhat/lwsmd.service \
		/etc/pbis/suse/lwsmd \
		/opt/pbis/include/krb5/krb5.h \
		/opt/pbis/include/krb5/locate_plugin.h \
		/opt/pbis/include/krb5/preauth_plugin.h \
		/opt/pbis/include/kdb.h \
		/opt/pbis/include/krb5.h \
		/opt/pbis/include/gssapi/gssapi_err_generic.h \
		/opt/pbis/include/gssapi/mechglue.h \
		/opt/pbis/include/gssapi/gssapi_ext.h \
		/opt/pbis/include/gssapi/gssapi_krb5.h \
		/opt/pbis/include/gssapi/gssapi_generic.h \
		/opt/pbis/include/gssapi/gssapi.h \
		/opt/pbis/include/profile.h \
		/opt/pbis/include/com_err.h \
		/opt/pbis/include/gssapi.h \
		/opt/pbis/include/sasl/md5global.h \
		/opt/pbis/include/sasl/sasl.h \
		/opt/pbis/include/sasl/hmac-md5.h \
		/opt/pbis/include/sasl/saslplug.h \
		/opt/pbis/include/sasl/md5.h \
		/opt/pbis/include/sasl/prop.h \
		/opt/pbis/include/sasl/saslutil.h \
		/opt/pbis/include/ldap_cdefs.h \
		/opt/pbis/include/lber_types.h \
		/opt/pbis/include/lber.h \
		/opt/pbis/include/slapi-plugin.h \
		/opt/pbis/include/ldap.h \
		/opt/pbis/include/ldap_utf8.h \
		/opt/pbis/include/ldap_features.h \
		/opt/pbis/include/ldap_schema.h \
		/opt/pbis/include/sqlite3.h \
		/opt/pbis/include/sqlite3ext.h \
		/opt/pbis/include/tdb.h \
		/opt/pbis/include/tchar.h \
		/opt/pbis/include/wchar16.h \
		/opt/pbis/include/wc16str.h \
		/opt/pbis/include/wc16printf.h \
		/opt/pbis/include/lwprintf.h \
		/opt/pbis/include/lw/dscache.h \
		/opt/pbis/include/lw/errno.h \
		/opt/pbis/include/lw/ntstatus.h \
		/opt/pbis/include/lw/winerror.h \
		/opt/pbis/include/lw/rpcstatus.h \
		/opt/pbis/include/lw/types.h \
		/opt/pbis/include/lw/attrs.h \
		/opt/pbis/include/lw/atomic.h \
		/opt/pbis/include/lw/hash.h \
		/opt/pbis/include/lw/rtllog.h \
		/opt/pbis/include/lw/rtlmemory.h \
		/opt/pbis/include/lw/rtlstring.h \
		/opt/pbis/include/lw/rtlgoto.h \
		/opt/pbis/include/lw/rbtree.h \
		/opt/pbis/include/lw/swab.h \
		/opt/pbis/include/lw/safeint.h \
		/opt/pbis/include/lw/security-types.h \
		/opt/pbis/include/lw/security-api.h \
		/opt/pbis/include/lw/threadpool.h \
		/opt/pbis/include/lw/affinity.h \
		/opt/pbis/include/lw/mapsecurity.h \
		/opt/pbis/include/lw/mapsecurity-types.h \
		/opt/pbis/include/lw/mapsecurity-plugin.h \
		/opt/pbis/include/lw/svcm.h \
		/opt/pbis/include/lw/base.h \
		/opt/pbis/include/lwmsg/call.h \
		/opt/pbis/include/lwmsg/message.h \
		/opt/pbis/include/lwmsg/data.h \
		/opt/pbis/include/lwmsg/assoc.h \
		/opt/pbis/include/lwmsg/context.h \
		/opt/pbis/include/lwmsg/time.h \
		/opt/pbis/include/lwmsg/buffer.h \
		/opt/pbis/include/lwmsg/connection.h \
		/opt/pbis/include/lwmsg/protocol.h \
		/opt/pbis/include/lwmsg/status.h \
		/opt/pbis/include/lwmsg/type.h \
		/opt/pbis/include/lwmsg/peer.h \
		/opt/pbis/include/lwmsg/security.h \
		/opt/pbis/include/lwmsg/common.h \
		/opt/pbis/include/lwmsg/session.h \
		/opt/pbis/include/lwmsg/archive.h \
		/opt/pbis/include/lwmsg/lwmsg.h \
		/opt/pbis/include/reg/lwntreg.h \
		/opt/pbis/include/reg/reg.h \
		/opt/pbis/include/reg/lwreg.h \
		/opt/pbis/include/reg/regutil.h \
		/opt/pbis/include/lwdef.h \
		/opt/pbis/include/lwerror.h \
		/opt/pbis/include/lwfile.h \
		/opt/pbis/include/lwkrb5.h \
		/opt/pbis/include/lwldap.h \
		/opt/pbis/include/lwmem.h \
		/opt/pbis/include/lwsecurityidentifier.h \
		/opt/pbis/include/lwstr.h \
		/opt/pbis/include/lwtime.h \
		/opt/pbis/include/lwsid.h \
		/opt/pbis/include/lwldap-error.h \
		/opt/pbis/include/lwdscache.h \
		/opt/pbis/include/lwhash.h \
		/opt/pbis/include/lwbuffer.h \
		/opt/pbis/include/lwdlinked-list.h \
		/opt/pbis/include/lwadvapi.h \
		/opt/pbis/include/lwnet.h \
		/opt/pbis/include/lwnet-plugin.h \
		/opt/pbis/include/lwio/io-types.h \
		/opt/pbis/include/lwio/io-types-posix.h \
		/opt/pbis/include/lwio/iortl.h \
		/opt/pbis/include/lwio/ntfileapi.h \
		/opt/pbis/include/lwio/smbfileapi.h \
		/opt/pbis/include/lwio/srvshareapi.h \
		/opt/pbis/include/lwio/srvtransportapi.h \
		/opt/pbis/include/lwio/lmfile.h \
		/opt/pbis/include/lwio/lmsession.h \
		/opt/pbis/include/lwio/lmshare.h \
		/opt/pbis/include/lwio/lmconnection.h \
		/opt/pbis/include/lwio/lwconnectioninfo.h \
		/opt/pbis/include/lwio/lwfileinfo.h \
		/opt/pbis/include/lwio/lwiofsctl.h \
		/opt/pbis/include/lwio/lwiodevctl.h \
		/opt/pbis/include/lwio/lwsessioninfo.h \
		/opt/pbis/include/lwio/lwshareinfo.h \
		/opt/pbis/include/lwio/iodriver.h \
		/opt/pbis/include/lwio/ioapi.h \
		/opt/pbis/include/lwio/lwzct.h \
		/opt/pbis/include/lwio/lwio.h \
		/opt/pbis/include/schtypes.h \
		/opt/pbis/include/schannel.h \
		/opt/pbis/include/dce/codesets_stub.h \
		/opt/pbis/include/dce/stubbase.h \
		/opt/pbis/include/dce/idl_es.h \
		/opt/pbis/include/dce/idlbase.h \
		/opt/pbis/include/dce/idlddefs.h \
		/opt/pbis/include/dce/rpcexc.h \
		/opt/pbis/include/dce/dce_utils.h \
		/opt/pbis/include/dce/sec_authn.h \
		/opt/pbis/include/dce/dce.h \
		/opt/pbis/include/dce/dce_error.h \
		/opt/pbis/include/dce/marshall.h \
		/opt/pbis/include/dce/ndr_rep.h \
		/opt/pbis/include/dce/ndrtypes.h \
		/opt/pbis/include/dce/dcethread.h \
		/opt/pbis/include/dce/linux-gnu/dce_error.h \
		/opt/pbis/include/dce/linux-gnu/dce.h \
		/opt/pbis/include/dce/x86_64/ndrtypes.h \
		/opt/pbis/include/dce/x86_64/ndr_rep.h \
		/opt/pbis/include/dce/x86_64/marshall.h \
		/opt/pbis/include/dce/codesets.h \
		/opt/pbis/include/dce/conv.h \
		/opt/pbis/include/dce/convc.h \
		/opt/pbis/include/dce/ep.h \
		/opt/pbis/include/dce/iovector.h \
		/opt/pbis/include/dce/lbase.h \
		/opt/pbis/include/dce/mgmt.h \
		/opt/pbis/include/dce/nbase.h \
		/opt/pbis/include/dce/ncastat.h \
		/opt/pbis/include/dce/ndrold.h \
		/opt/pbis/include/dce/rpcbase.h \
		/opt/pbis/include/dce/rpcpvt.h \
		/opt/pbis/include/dce/rpcsts.h \
		/opt/pbis/include/dce/rpctypes.h \
		/opt/pbis/include/dce/twr.h \
		/opt/pbis/include/dce/uuid.h \
		/opt/pbis/include/dce/id_base.h \
		/opt/pbis/include/dce/schannel.h \
		/opt/pbis/include/dce/smb.h \
		/opt/pbis/include/dce/lrpc.h \
		/opt/pbis/include/dce/rpc.h \
		/opt/pbis/include/dce/codesets.idl \
		/opt/pbis/include/dce/conv.idl \
		/opt/pbis/include/dce/convc.idl \
		/opt/pbis/include/dce/ep.idl \
		/opt/pbis/include/dce/iovector.idl \
		/opt/pbis/include/dce/lbase.idl \
		/opt/pbis/include/dce/mgmt.idl \
		/opt/pbis/include/dce/nbase.idl \
		/opt/pbis/include/dce/ncastat.idl \
		/opt/pbis/include/dce/ndrold.idl \
		/opt/pbis/include/dce/rpc.idl \
		/opt/pbis/include/dce/rpcbase.idl \
		/opt/pbis/include/dce/rpcpvt.idl \
		/opt/pbis/include/dce/rpcsts.idl \
		/opt/pbis/include/dce/rpctypes.idl \
		/opt/pbis/include/dce/twr.idl \
		/opt/pbis/include/dce/uuid.idl \
		/opt/pbis/include/dce/id_base.idl \
		/opt/pbis/include/compat/rpcfields.h \
		/opt/pbis/include/compat/baserpc.h \
		/opt/pbis/include/compat/dce2msrpc.h \
		/opt/pbis/include/compat/dcerpc.h \
		/opt/pbis/include/lwrpcrt/lwrpcrt.h \
		/opt/pbis/include/ctarray.h \
		/opt/pbis/include/ctdef.h \
		/opt/pbis/include/ctexec.h \
		/opt/pbis/include/ctfileutils.h \
		/opt/pbis/include/cthash.h \
		/opt/pbis/include/ctmem.h \
		/opt/pbis/include/ctprocutils.h \
		/opt/pbis/include/ctrwlock.h \
		/opt/pbis/include/ctshell.h \
		/opt/pbis/include/ctstrutils.h \
		/opt/pbis/include/ctsys.h \
		/opt/pbis/include/cttext.h \
		/opt/pbis/include/ctuser.h \
		/opt/pbis/include/lwexc.h \
		/opt/pbis/include/ctsysfuncs.h \
		/opt/pbis/include/ctbase.h \
		/opt/pbis/include/lwsm/lwsm.h \
		/opt/pbis/include/adtool/types.h \
		/opt/pbis/include/eventlog.h \
		/opt/pbis/include/eventlog-record.h \
		/opt/pbis/include/lsa/provider.h \
		/opt/pbis/include/lsa/lsa.h \
		/opt/pbis/include/lsa/lsapstore-types.h \
		/opt/pbis/include/lsa/lsapstore-plugin.h \
		/opt/pbis/include/lsa/lsapstore-api.h \
		/opt/pbis/include/lsa/ad-types.h \
		/opt/pbis/include/lsa/ad.h \
		/opt/pbis/include/lsa/privilege.h \
		/opt/pbis/include/ntlm/gssntlm.h \
		/opt/pbis/include/ntlm/sspintlm.h \
		/opt/pbis/include/lw/rpc/common.h \
		/opt/pbis/include/lw/rpc/lsa.h \
		/opt/pbis/include/lw/rpc/samr.h \
		/opt/pbis/include/lw/rpc/netlogon.h \
		/opt/pbis/include/lw/rpc/dssetup.h \
		/opt/pbis/include/lw/rpc/krb5pac.h \
		/opt/pbis/include/lw/rpc/wkssvc.h \
		/opt/pbis/include/lsa/internal/lsaadprovider.h \
		/opt/pbis/include/lsa/internal/lsalocalprovider.h \
		/opt/pbis/include/lsa/internal/lsadatablob.h \
		/opt/pbis/include/lsa/internal/lsadef.h \
		/opt/pbis/include/lsa/internal/lsaipc-common.h \
		/opt/pbis/include/lsa/internal/lsaipc.h \
		/opt/pbis/include/lsa/internal/lsaipc-privilege.h \
		/opt/pbis/include/lsa/internal/lsaprivilege-internal.h \
		/opt/pbis/include/lsa/internal/lsalist.h \
		/opt/pbis/include/lsa/internal/lsasrvcred.h \
		/opt/pbis/include/lsa/internal/lsasystem.h \
		/opt/pbis/include/lsa/internal/lsautils.h \
		/opt/pbis/include/lsa/internal/lwsecurityidentifier.h \
		/opt/pbis/include/lsa/internal/machinepwdinfo-impl.h \
		/opt/pbis/include/lsa/internal/xpg_socket.h \
		/opt/pbis/include/lsa/internal/lsasrvapi.h \
		/opt/pbis/include/lsa/internal/lsasrvutils.h \
		/opt/pbis/include/lwdns.h \
		/opt/pbis/include/lw/lmaccess.h \
		/opt/pbis/include/lw/lmcreds.h \
		/opt/pbis/include/lw/lmcrypt.h \
		/opt/pbis/include/lw/lmdebug.h \
		/opt/pbis/include/lw/lmerr.h \
		/opt/pbis/include/lw/lmjoin.h \
		/opt/pbis/include/lw/lmmem.h \
		/opt/pbis/include/lw/lmshare.h \
		/opt/pbis/include/lw/lmwksta.h \
		/opt/pbis/include/lw/lmserver.h \
		/opt/pbis/include/lw/lm.h \
		/opt/pbis/include/OpenSOAP/Block.h \
		/opt/pbis/include/OpenSOAP/ByteArray.h \
		/opt/pbis/include/OpenSOAP/CStdio.h \
		/opt/pbis/include/OpenSOAP/ClientSocket.h \
		/opt/pbis/include/OpenSOAP/Defines.h \
		/opt/pbis/include/OpenSOAP/Envelope.h \
		/opt/pbis/include/OpenSOAP/ErrorCode.h \
		/opt/pbis/include/OpenSOAP/Locale.h \
		/opt/pbis/include/OpenSOAP/OpenSOAP.h \
		/opt/pbis/include/OpenSOAP/Serializer.h \
		/opt/pbis/include/OpenSOAP/Service.h \
		/opt/pbis/include/OpenSOAP/Security.h \
		/opt/pbis/include/OpenSOAP/Stream.h \
		/opt/pbis/include/OpenSOAP/String.h \
		/opt/pbis/include/OpenSOAP/StringHash.h \
		/opt/pbis/include/OpenSOAP/Transport.h \
		/opt/pbis/include/OpenSOAP/XMLAttr.h \
		/opt/pbis/include/OpenSOAP/XMLElm.h \
		/opt/pbis/include/OpenSOAP/XMLNamespace.h \
		/opt/pbis/include/djdistroinfo.h \
		/opt/pbis/lib/libcom_err.so \
		/opt/pbis/lib/libk5crypto.so \
		/opt/pbis/lib/libkadm5srv_mit.so \
		/opt/pbis/lib/libgssrpc.so \
		/opt/pbis/lib/libkrb5support.so \
		/opt/pbis/lib/libcom_err.la \
		/opt/pbis/lib/libk5crypto.la \
		/opt/pbis/lib/libgssapi_krb5.la \
		/opt/pbis/lib/libkrb5.la \
		/opt/pbis/lib/libkadm5srv_mit.la \
		/opt/pbis/lib/libkdb5.la \
		/opt/pbis/lib/libgssrpc.la \
		/opt/pbis/lib/libkrb5support.la \
		/opt/pbis/lib/libsasl2.la \
		/opt/pbis/lib/libldap.so \
		/opt/pbis/lib/libldap_r.so \
		/opt/pbis/lib/liblber.so \
		/opt/pbis/lib/libldap.la \
		/opt/pbis/lib/libldap_r.la \
		/opt/pbis/lib/liblber.la \
		/opt/pbis/lib/libsqlite3.la \
		/opt/pbis/lib/libtdb.so \
		/opt/pbis/lib/libtdb.la \
		/opt/pbis/lib/liblwbase_nothr.so \
		/opt/pbis/lib/liblwbase_nothr.la \
		/opt/pbis/lib/liblwbase.so \
		/opt/pbis/lib/liblwbase.la \
		/opt/pbis/lib/liblwmsg_nothr.so \
		/opt/pbis/lib/liblwmsg_nothr.la \
		/opt/pbis/lib/liblwmsg.so \
		/opt/pbis/lib/liblwmsg.la \
		/opt/pbis/lib/libregcommon.so \
		/opt/pbis/lib/libregcommon.la \
		/opt/pbis/lib/libregclient.so \
		/opt/pbis/lib/libregclient.la \
		/opt/pbis/lib/librsutils.so \
		/opt/pbis/lib/librsutils.la \
		/opt/pbis/lib/liblwadvapi.so \
		/opt/pbis/lib/liblwadvapi.la \
		/opt/pbis/lib/liblwadvapi_nothr.so \
		/opt/pbis/lib/liblwadvapi_nothr.la \
		/opt/pbis/lib/liblwnetcommon.so \
		/opt/pbis/lib/liblwnetcommon.la \
		/opt/pbis/lib/liblwnetclientapi.so \
		/opt/pbis/lib/liblwnetclientapi.la \
		/opt/pbis/lib/liblwiocommon.so \
		/opt/pbis/lib/liblwiocommon.la \
		/opt/pbis/lib/liblwioshareinfo.so \
		/opt/pbis/lib/liblwioshareinfo.la \
		/opt/pbis/lib/liblwioclient.so \
		/opt/pbis/lib/liblwioclient.la \
		/opt/pbis/lib/libiomgr.so \
		/opt/pbis/lib/libiomgr.la \
		/opt/pbis/lib/liblwiosmbcommon.so \
		/opt/pbis/lib/liblwiosmbcommon.la \
		/opt/pbis/lib/libiotest.sys.so \
		/opt/pbis/lib/libiotest.sys.la \
		/opt/pbis/lib/libschannel.so \
		/opt/pbis/lib/libschannel.la \
		/opt/pbis/lib/libdcerpc.so \
		/opt/pbis/lib/libdcerpc.la \
		/opt/pbis/lib/libcentutils.so \
		/opt/pbis/lib/libcentutils.la \
		/opt/pbis/lib/liblwsmcommon.so \
		/opt/pbis/lib/liblwsmcommon.la \
		/opt/pbis/lib/liblwsm.so \
		/opt/pbis/lib/liblwsm.la \
		/opt/pbis/lib/libadtool.so \
		/opt/pbis/lib/libadtool.la \
		/opt/pbis/lib/libeventlogutils.so \
		/opt/pbis/lib/libeventlogutils.la \
		/opt/pbis/lib/libeventlog.so \
		/opt/pbis/lib/libeventlog.la \
		/opt/pbis/lib/libeventlog_norpc.so \
		/opt/pbis/lib/libeventlog_norpc.la \
		/opt/pbis/lib/liblsacommon.so \
		/opt/pbis/lib/liblsacommon.la \
		/opt/pbis/lib/liblsapstore.so \
		/opt/pbis/lib/liblsapstore.la \
		/opt/pbis/lib/liblsaclient.so \
		/opt/pbis/lib/liblsaclient.la \
		/opt/pbis/lib/liblsaclientthr.so \
		/opt/pbis/lib/liblsaclientthr.la \
		/opt/pbis/lib/liblsaclient_ntlm.so \
		/opt/pbis/lib/liblsaclient_ntlm.la \
		/opt/pbis/lib/liblsarpc.so \
		/opt/pbis/lib/liblsarpc.la \
		/opt/pbis/lib/liblsaauth.so \
		/opt/pbis/lib/liblsaauth.la \
		/opt/pbis/lib/liblsagsswrap.so \
		/opt/pbis/lib/liblsagsswrap.la \
		/opt/pbis/lib/liblsaserverapi.so \
		/opt/pbis/lib/liblsaserverapi.la \
		/opt/pbis/lib/libntlmserver.so \
		/opt/pbis/lib/libntlmserver.la \
		/opt/pbis/lib/libdsapi.so \
		/opt/pbis/lib/libdsapi.la \
		/opt/pbis/lib/liblwdns.so \
		/opt/pbis/lib/liblwdns.la \
		/opt/pbis/lib/liblwnetapi.so \
		/opt/pbis/lib/liblwnetapi.la \
		/opt/pbis/lib/libOpenSOAPClient.so \
		/opt/pbis/lib/libOpenSOAPSecurity.so \
		/opt/pbis/lib/libOpenSOAPService.so \
		/opt/pbis/lib/libOpenSOAPClient.la \
		/opt/pbis/lib/libOpenSOAPSecurity.la \
		/opt/pbis/lib/libOpenSOAPService.la \
		/opt/pbis/lib/libdomainjoin.so \
		/opt/pbis/lib/libdomainjoin.la \
		/opt/pbis/lib/libwbclient.so \
		/opt/pbis/lib/libwbclient.la \
		/opt/pbis/lib/lwicompat_v4.la
do
	if [ ! -d $(dirname %{buildroot}$FILE) ]; then
		mkdir -p $(dirname %{buildroot}$FILE)
	fi
	cp -a transformerbuild/stage$FILE %{buildroot}$FILE
done

install -m 755 config/upgrade-likewise-to-pbis %{buildroot}/opt/pbis/libexec
mkdir -p -m 755 %{buildroot}/%{_unitdir}
install -m 644 config/upgrade-likewise-to-pbis.service %{buildroot}/%{_unitdir}

%define AdProviderPath /opt/pbis/lib/lsa-provider/ad_open.so
%post
DAEMONS_TO_HALT="reapsysld lsassd lwiod netlogond eventlogd dcerpcd lwregd lwsmd"

UPGRADEDIR=/var/lib/pbis-upgrade
PKG_ARCH="x86_64"

LOG=/var/log/pbis-open-install.log

# Display to screen and log file with a blank line between entries.
log()
{
    echo $@
    echo
    echo $@ >> $LOG
    echo >> $LOG
}

# Display to screen and log file with no blank line.
_log()
{
    echo $@
    echo $@ >> $LOG
}

# Display to file.
logfile()
{
    echo $@ >> $LOG
    echo >> $LOG
}

# Execute command.
# If successful, note in log file.
# If not successful, note on screen and log file.
run()
{
    tlog=$("$@" 2>&1)
    err=$?
    if [ $err -eq 0 ]; then
        echo "Success: $@" >> $LOG
        echo "$tlog" >> $LOG
        echo >> $LOG
    else
        _log "Error: $@ returned $err"
        _log "$tlog"
        _log
    fi
    return $err
}

# Execute command.
# Log only to file.
run_quiet()
{
    tlog=$("$@" 2>&1)
    err=$?
    if [ $err -eq 0 ]; then
        echo "Success: $@" >> $LOG
    else
        echo "Error: $@ returned $err  (ignoring and continuing)" >> $LOG
    fi
    echo "$tlog" >> $LOG
    echo >> $LOG
    return $err
}

# Execute command.
# If successful, note in log file.
# If not successful, note on screen and log file and then exit.
run_or_fail()
{
    tlog=$("$@" 2>&1)
    err=$?
    if [ $err -eq 0 ]; then
        echo "Success: $@" >> $LOG
        echo "$tlog" >> $LOG
        echo >> $LOG
    else
        _log "Error: $@ returned $err  (aborting this script)"
        _log "$tlog"
        _log
        exit 1
    fi
    return $err
}

import_registry_configurations()
{
    REGSHELL='/opt/pbis/bin/regshell'

    log 'Importing registry...'
    for i in "/opt/pbis/share/config/"*.reg
    do
echo $i
        run_or_fail "$REGSHELL" import "$i"
    done
}

determine_os_version()
{
    PBIS_DISTRO=unknown
    PBIS_DISTRO_VERSION=unknown

    if [ -f '/etc/centos-release' ]; then
        PBIS_DISTRO=centos
        if [ -n "`grep '^CentOS release 7' '/etc/centos-release'`" ]; then
            PBIS_DISTRO_VERSION=7.0
        elif [ -n "`grep '^CentOS Linux release 7' '/etc/centos-release'`" ]; then
            PBIS_DISTRO_VERSION=7.0
        elif [ -n "`grep '^CentOS release 6' '/etc/centos-release'`" ]; then
            PBIS_DISTRO_VERSION=6.0
        elif [ -n "`grep '^CentOS Linux release 6' '/etc/centos-release'`" ]; then
            PBIS_DISTRO_VERSION=6.0
        elif [ -n "`grep '^CentOS release 5' '/etc/centos-release'`" ]; then
            PBIS_DISTRO_VERSION=5.0
        fi
    elif [ -f '/etc/fedora-release' ]; then
        PBIS_DISTRO=fedora
        if [ -n "`grep '^Fedora release 20 ' '/etc/fedora-release'`" ]; then
            PBIS_DISTRO_VERSION=19
        elif [ -n "`grep '^Fedora release 19 ' '/etc/fedora-release'`" ]; then
            PBIS_DISTRO_VERSION=19
        elif [ -n "`grep '^Fedora release 18 ' '/etc/fedora-release'`" ]; then
            PBIS_DISTRO_VERSION=18
        elif [ -n "`grep '^Fedora release 17 ' '/etc/fedora-release'`" ]; then
            PBIS_DISTRO_VERSION=17
        elif [ -n "`grep '^Fedora release 16 ' '/etc/fedora-release'`" ]; then
            PBIS_DISTRO_VERSION=16
        elif [ -n "`grep '^Fedora release 15 ' '/etc/fedora-release'`" ]; then
            PBIS_DISTRO_VERSION=15
        elif [ -n "`grep '^Fedora release 14 ' '/etc/fedora-release'`" ]; then
            PBIS_DISTRO_VERSION=14
        elif [ -n "`grep '^Fedora release 13 ' '/etc/fedora-release'`" ]; then
            PBIS_DISTRO_VERSION=13
        fi
    elif [ -f '/etc/redhat-release' ]; then
        if [ -n "`grep '^CentOS release 5' '/etc/redhat-release'`" ]; then
            PBIS_DISTRO=centos
            PBIS_DISTRO_VERSION=5.0
        elif [ -n "`grep '^Red Hat Enterprise Linux Server release 5' '/etc/redhat-release'`" ]; then
            PBIS_DISTRO=rhel
            PBIS_DISTRO_VERSION=5.0
        elif [ -n "`grep '^Red Hat Enterprise Linux Server release 6' '/etc/redhat-release'`" ]; then
            PBIS_DISTRO=rhel
            PBIS_DISTRO_VERSION=6.0
        elif [ -n "`grep '^Red Hat Enterprise Linux Workstation release 6' '/etc/redhat-release'`" ]; then
            PBIS_DISTRO=rhel
            PBIS_DISTRO_VERSION=6.0
        elif [ -n "`grep '^Red Hat Enterprise Linux release 6' '/etc/redhat-release'`" ]; then
            PBIS_DISTRO=rhel
            PBIS_DISTRO_VERSION=6.0
        elif [ -n "`grep '^Red Hat Enterprise Linux release 7' '/etc/redhat-release'`" ]; then
            PBIS_DISTRO=rhel
            PBIS_DISTRO_VERSION=7.0
        elif [ -n "`grep '^Red Hat Enterprise Linux Server release 7' '/etc/redhat-release'`" ]; then
            PBIS_DISTRO=rhel
            PBIS_DISTRO_VERSION=7.0
        elif [ -n "`grep '^Red Hat Enterprise Linux Workstation release 7' '/etc/redhat-release'`" ]; then
            PBIS_DISTRO=rhel
            PBIS_DISTRO_VERSION=7.0
        fi
    fi
}

setup_selinux_policy_module()
{
    DISTRO=$PBIS_DISTRO
    VERSION=$PBIS_DISTRO_VERSION

    # CentOS uses the same policy as RedHat Enterprise
    if [ "$DISTRO" = "centos" ]; then
        DISTRO="rhel"
    fi

    logfile "DISTRO=$DISTRO VERSION=$PBIS_DISTRO_VERSION"
    if [ ! -x "/usr/sbin/semodule" ]; then
        logfile "/usr/sbin/semodule not present."
        return;
    fi

    if [ ! -d "/etc/selinux/targeted/policy" ]; then
        logfile "/etc/selinux/targeted/policy not present."
        return;
    fi

    if [ "$DISTRO" = "rhel" -a "$VERSION" = "5.0" ]; then
        log 'SELinux Policy Module not required.'
    elif [ -f "/opt/pbis/share/pbis.pp" ]; then
        log 'Setting up SELinux Policy Module using /opt/pbis/share/pbis.pp'
        run_or_fail /usr/sbin/semodule -i "/opt/pbis/share/pbis.pp"
        run_quiet /sbin/fixfiles -R pbis-open restore
    elif [ -f "/opt/pbis/share/$DISTRO/$VERSION/pbis.pp" ]; then
        log 'Setting up SELinux Policy Module'
        run_or_fail /usr/sbin/semodule -i "/opt/pbis/share/$DISTRO/$VERSION/pbis.pp"
        run_quiet /sbin/fixfiles -R pbis-open restore
    else
      log "An appropriate SELinux policy [/opt/pbis/share/$DISTRO/$VERSION/pbis.pp] was not included in this package.
You may provide a policy at /opt/pbis/share/pbis.pp"
      if [ -x "/usr/sbin/selinuxenabled" -a -x "/usr/sbin/getenforce" ]; then
        logfile "/usr/sbin/selinuxenabled and /usr/sbin/getenforce are present"
        if /usr/sbin/selinuxenabled >/dev/null 2>&1; then
            logfile "selinuxenabled indicates SELinux is enabled"
            if /usr/sbin/getenforce 2>&1 | grep -v 'Permissive' >/dev/null 2>&1; then
                if [ -f /etc/selinux/config ]; then                 
                    log "SELinux found to be present, enabled, and enforcing.
You may either provide a policy at /opt/pbis/share/pbis.pp  --OR--
SELinux must be disabled or set to permissive mode by editing the file
/etc/selinux/config and rebooting.
For instructions on how to edit the file to disable SELinux, see the SELinux man page."
                else
                    log "SELinux found to be present, enabled, and enforcing.
You may either provide a policy at /opt/pbis/share/pbis.pp  --OR--
SELinux must be disabled or set to permissive mode.
Check your system's documentation for details."
                fi
                log 'PowerBroker Identity Services will not install without an appropriate policy for SELinux.'
                exit 1
            else
                logfile "getenforce indicates permissive (which is ok)"
            fi
        else
            logfile "selinuxenabled indicates SELinux is not enabled"
        fi
      fi
    fi
}

determine_upgrade_type()
{
    PRESERVEDVERSIONFILE="${UPGRADEDIR}/VERSION"

    if [ -f "$PRESERVEDVERSIONFILE" ]; then
        run_or_fail cat "$PRESERVEDVERSIONFILE"
        if [ -n "`grep '^VERSION=5.0' $PRESERVEDVERSIONFILE`" ]; then
            UPGRADING_FROM_5_0123=1
            log 'Upgrading from Likewise Identity Services Open 5.0'
        elif [ -n "`grep '^VERSION=5.1' $PRESERVEDVERSIONFILE`" ]; then
            UPGRADING_FROM_5_0123=1
            log 'Upgrading from Likewise Identity Services Open 5.1'
        elif [ -n "`grep '^VERSION=5.2' $PRESERVEDVERSIONFILE`" ]; then
            UPGRADING_FROM_5_0123=1
            log 'Upgrading from Likewise Identity Services Open 5.2'
        elif [ -n "`grep '^VERSION=5.3' $PRESERVEDVERSIONFILE`" ]; then
            UPGRADING_FROM_5_0123=1
            log 'Upgrading from Likewise Identity Services Open 5.3'
        elif [ -n "`grep '^VERSION=5.4' $PRESERVEDVERSIONFILE`" ]; then
            # 5.4 not released but used by OEMs.
            #UPGRADING_FROM_5_0123=1
            UPGRADING_FROM_6_0=1
            log 'Upgrading from Likewise Identity Services Open 5.4'
        elif [ -n "`grep '^VERSION=6.0' $PRESERVEDVERSIONFILE`" ]; then
            UPGRADING_FROM_6_0=1
            log 'Upgrading from Likewise Open 6.0'
        elif [ -n "`grep '^VERSION=6.1' $PRESERVEDVERSIONFILE`" ]; then
            UPGRADING_FROM_6_1=1
            log 'Upgrading from Likewise Open 6.1'
        elif [ -n "`grep '^VERSION=6.5' $PRESERVEDVERSIONFILE`" ]; then
            UPGRADING_FROM_6_5=1
            log 'Upgrading from PowerBroker Identity Services Open 6.5'
        fi
    fi
}

determine_join_status()
{
    STATUSFILE="${UPGRADEDIR}/status.txt"

    if [ -f "${UPGRADEDIR}/status.txt" ]; then
        run_or_fail cat "$STATUSFILE"

        domain=`cat $STATUSFILE 2>/dev/null | grep '^STATUS_JOINED=' | sed -e 's/STATUS_JOINED=//'`

        if [ -n "$domain" ]; then
            logfile "Found domain $domain in status file."
            result=$domain
        else
            result=""
        fi
    fi

    if [ -z "$result" ]; then
        domain=`/opt/pbis/bin/lsa ad-get-machine account 2>/dev/null | grep '  DNS Domain Name: ' | sed -e 's/  DNS Domain Name: //'`
        if [ -n "$domain" ]; then
            logfile "Found domain $domain using ad-get-machine account"
            result=$domain
        else
            result=""
        fi
    fi
    if [ -z "$result" ]; then
        SQLITE="/usr/bin/sqlite3"
        if [ -x /opt/pbis/bin/sqlite3 ]; then
            SQLITE="/opt/pbis/bin/sqlite3"
        elif [ -x /opt/likewise/bin/sqlite3 ]; then
            SQLITE="/opt/likewise/bin/sqlite3"
        fi
        if [ -n "$SQLITE" ]; then
          if [ -f "${UPGRADEDIR}/registry.db" ]; then
            domain=`$SQLITE ${UPGRADEDIR}/registry.db .dump | perl -n -MEncode=decode -e "next unless(/DnsDomainName/); /X'([0-9A-F]+)'/; "'$x=decode("UCS2-LE", pack("H*", $1)); if ($x) { print $x, "\n"; exit; }'`
            # using dump instead of sqlite3 ./registry.db 'select quote(Value) from regvalues1 where ValueName = "DnsDomainName";' | perl -ne "s/[X']//g; chomp; "'print pack("H*", $_), "\n";'
            # because the select gets additional fields from the netlogon cache we don't want that corrupt the data (trusted domains, not ours)
            if [ -n "$domain" ]; then
                logfile "Found domain $domain using $SQLITE .dump"
                result=$domain
            else
                result=""
            fi
          else
            result=""
          fi
        fi
    fi


}

import_5_0123_file()
{
    CONVERT='/opt/pbis/libexec/conf2reg'
    REGSHELL='/opt/pbis/bin/regshell'

    COMMAND=$1
    SOURCE=$2
    # DEST is not necessary for some commands.
    DEST=$3

    if [ -f "$SOURCE" ]; then
        run_quiet "$CONVERT" "$COMMAND" "$SOURCE" $DEST
        if [ $? -ne 0 ]; then
            log "There was a problem converting $SOURCE. Please file a bug and attach $SOURCE."
            return 1
        fi

        if [ -n "$DEST" -a -f "$DEST" ]; then
            run_quiet "$REGSHELL" import "$DEST"
            if [ $? -ne 0 ]; then
                log "There was a problem converting $SOURCE. Please file a bug and attach $SOURCE and $DEST."
                return 1
            fi
        fi
    fi
    return 0
}

restore_5_0123_configuration()
{
    if [ -z "$UPGRADING_FROM_5_0123" ]; then
        return 0
    fi

    import_5_0123_file --lsass "${UPGRADEDIR}/lsassd.conf" \
        "${UPGRADEDIR}/lsassd.conf.reg"

    import_5_0123_file --netlogon "${UPGRADEDIR}/netlogon.conf" \
        "${UPGRADEDIR}/netlogon.conf.reg"

    import_5_0123_file --eventlog "${UPGRADEDIR}/eventlogd.conf" \
        "${UPGRADEDIR}/eventlogd.conf.reg"

    import_5_0123_file --pstore-sqlite "${UPGRADEDIR}/pstore.db"
}

restore_6_0_configuration()
{
    if [ -z "$UPGRADING_FROM_6_0" ]; then
        return 0
    fi

    run_or_fail mkdir -p '/var/lib/pbis/db'
    run_or_fail chmod 700 '/var/lib/pbis/db'
    run_or_fail chown 0 '/var/lib/pbis/db'

    if [ -f "${UPGRADEDIR}/registry.db" ]; then
        run_or_fail cp "${UPGRADEDIR}/registry.db" '/var/lib/pbis/db/registry.db'
        run_or_fail chmod 700 '/var/lib/pbis/db/registry.db'
    fi

    if [ -f "${UPGRADEDIR}/sam.db" ]; then
        run_or_fail cp "${UPGRADEDIR}/sam.db" '/var/lib/pbis/db/sam.db'
        run_or_fail chmod 700 '/var/lib/pbis/db/sam.db'
    fi

    if [ -f "${UPGRADEDIR}/lwi_events.db" ]; then
        run_or_fail cp "${UPGRADEDIR}/lwi_events.db" '/var/lib/pbis/db/lwi_events.db'
        run_or_fail chmod 644 '/var/lib/pbis/db/lwi_events.db'
    fi

    if [ -f "${UPGRADEDIR}/lsass-adcache.db" ]; then
        run_or_fail cp "${UPGRADEDIR}/lsass-adcache.db" '/var/lib/pbis/db/lsass-adcache.db'
        run_or_fail chmod 700 '/var/lib/pbis/db/lsass-adcache.db'
    fi

    if [ -f "${UPGRADEDIR}/lsass-adcache.filedb" ]; then
        determine_join_status
        if [ -n "$result" ]; then
            DOMAIN="$result"
            run_or_fail cp "${UPGRADEDIR}/lsass-adcache.filedb" "/var/lib/pbis/db/lsass-adcache.filedb.${DOMAIN}"
            run_or_fail chmod 700 "/var/lib/pbis/db/lsass-adcache.filedb.${DOMAIN}"
        else
            run_or_fail cp "${UPGRADEDIR}/lsass-adcache.filedb" '/var/lib/pbis/db/lsass-adcache.filedb'
            run_or_fail chmod 700 '/var/lib/pbis/db/lsass-adcache.filedb'
        fi
    fi

    run_quiet rm -r "${UPGRADEDIR}"
}

restore_6_1_configuration()
{
    if [ -z "$UPGRADING_FROM_6_1" ]; then
        return 0
    fi

    run_or_fail mkdir -p '/var/lib/pbis/db'
    run_or_fail chmod 700 '/var/lib/pbis/db'
    run_or_fail chown 0 '/var/lib/pbis/db'

    if [ -f "${UPGRADEDIR}/registry.db" ]; then
        run_or_fail cp "${UPGRADEDIR}/registry.db" '/var/lib/pbis/db/registry.db'
        run_or_fail chmod 700 '/var/lib/pbis/db/registry.db'
    fi

    if [ -f "${UPGRADEDIR}/sam.db" ]; then
        run_or_fail cp "${UPGRADEDIR}/sam.db" '/var/lib/pbis/db/sam.db'
        run_or_fail chmod 700 '/var/lib/pbis/db/sam.db'
    fi

    if [ -f "${UPGRADEDIR}/lwi_events.db" ]; then
        run_or_fail cp "${UPGRADEDIR}/lwi_events.db" '/var/lib/pbis/db/lwi_events.db'
        run_or_fail chmod 644 '/var/lib/pbis/db/lwi_events.db'
    fi

    if [ -f "${UPGRADEDIR}/lsass-adcache.db" ]; then
        run_or_fail cp "${UPGRADEDIR}/lsass-adcache.db" '/var/lib/pbis/db/lsass-adcache.db'
        run_or_fail chmod 700 '/var/lib/pbis/db/lsass-adcache.db'
    fi

    for cache in "${UPGRADEDIR}"/lsass-adcache.filedb.* ; do
        if [ -f "$cache" ]; then
            cachefile=`basename $cache`
            run_or_fail cp "${cache}" "/var/lib/pbis/db/${cachefile}"
            run_or_fail chmod 700 "/var/lib/pbis/db/${cachefile}"
        fi
    done

    run_quiet rm -r "${UPGRADEDIR}"
}

remove_old_init_symlinks()
{
    for daemon in dcerpcd netlogond eventlogd lwiod lsassd gpagentd; do
        rm -f /etc/rc?.d/*"$daemon"
    done
}

relocate_domain_separator()
{
    DomainSeparator=`/opt/pbis/bin/regshell list_values '[HKEY_THIS_MACHINE\Services\lsass\Parameters\Providers\ActiveDirectory]' | grep DomainSeparator | sed -e 's/ *[^ ]\+[ ]\+[^ ]\+[ ]\+"\([^ ]*\)"$/\1/'`

    if [ -n "${DomainSeparator}" ]; then
        if [ "$DomainSeparator" = "\\\\" ]; then
            DomainSeparator="\\"
        fi

        run_quiet '/opt/pbis/bin/regshell' set_value '[HKEY_THIS_MACHINE\Services\lsass\Parameters]' 'DomainSeparator' "$DomainSeparator"
    fi
}

relocate_space_replacement()
{
    SpaceReplacement=`/opt/pbis/bin/regshell list_values '[HKEY_THIS_MACHINE\Services\lsass\Parameters\Providers\ActiveDirectory]' | grep SpaceReplacement | sed -e 's/ *[^ ]\+[ ]\+[^ ]\+[ ]\+"\([^ ]*\)"$/\1/'`

    if [ -n "${SpaceReplacement}" ]; then
        run_quiet '/opt/pbis/bin/regshell' set_value '[HKEY_THIS_MACHINE\Services\lsass\Parameters]' 'SpaceReplacement' "$SpaceReplacement"
    fi
}

remove_npfs_dependencies()
{
    run_quiet '/opt/pbis/bin/regshell' set_value '[HKEY_THIS_MACHINE\Services\lwio\Parameters\Drivers]' 'Load' 'rdr'
    run_quiet '/opt/pbis/bin/regshell' set_value '[HKEY_THIS_MACHINE\Services\lsass]' 'Dependencies' 'netlogon lwio lwreg rdr'
}

remove_dcerpc_dependencies()
{
   run_quiet '/opt/pbis/bin/regshell' set_value '[HKEY_THIS_MACHINE\Services\eventlog]' 'Dependencies' ''
   run_quiet '/opt/pbis/bin/regshell' delete_value '[HKEY_THIS_MACHINE\Services\dcerpc]'  'Autostart'
   run_quiet '/opt/pbis/bin/regshell' set_value '[HKEY_THIS_MACHINE\Services\dcerpc]'  'Arguments' ''
}

remove_TrustEnumerationWaitSettingFromADPath()
{
    run_quiet '/opt/pbis/bin/regshell' delete_value '[HKEY_THIS_MACHINE\Services\lsass\Parameters\Providers\ActiveDirectory]' 'TrustEnumerationWait'
    run_quiet '/opt/pbis/bin/regshell' delete_value '[HKEY_THIS_MACHINE\Services\lsass\Parameters\Providers\ActiveDirectory]'  'TrustEnumerationWaitSeconds'
}

fix_60_registry()
{
    REGSHELL='/opt/pbis/bin/regshell'

    if [ -z "$UPGRADING_FROM_6_0" ]; then
        return 0
    fi

    # Migrate pstore entries from default to joined domain
    run '/opt/pbis/libexec/regupgr61.sh' --install

    # Migrate some other entries
    relocate_domain_separator
    relocate_space_replacement

}

cleanup_registry()
{
    for i in "/opt/pbis/share/config/"*.reg
    do
        run_or_fail "${REGSHELL}" cleanup "$i"
    done
}

switch_to_open_provider()
{
    _value='[HKEY_THIS_MACHINE\Services\lsass\Parameters\Providers\ActiveDirectory]'
    _path='%{AdProviderPath}'

    run_quiet '/opt/pbis/bin/regshell' set_value "$_value" Path "$_path"
}

execute_auxiliary_scripts()
{
    # The system administrator may have configured these during a previous
    # install
    if [ -d "/var/lib/pbis/scripts/install" ]; then
        for file in /var/lib/pbis/scripts/install/*; do
            run_quiet "$file" --install
        done
    fi
}

symlink_pam_lsass()
{
    if [ ! -e "/lib64/security/pam_lsass.so" ]; then
        run ln -s /lib/security/pam_lsass.so /lib64/security/pam_lsass.so
    fi
}

postinstall()
{
    logfile "Package: PowerBroker Identity Services Open postinstall begins (`date`)"
    echo "in postinstall"

    determine_os_version

    setup_selinux_policy_module

    determine_upgrade_type

    restore_6_0_configuration

    restore_6_1_configuration
 
    run_or_fail '/opt/pbis/sbin/lwsmd' --start-as-daemon --disable-autostart --loglevel debug

    restore_5_0123_configuration

    import_registry_configurations

    fix_60_registry

    cleanup_registry

    #remove_TrustEnumerationWaitSettingFromADPath

    remove_npfs_dependencies

    remove_dcerpc_dependencies

    switch_to_open_provider

    #CA-208359: PBIS services should start on-demand in dom0, disable EventlogAutostart 
    run_quiet /opt/pbis/bin/config EventlogAutostart false
    
    run_or_fail '/opt/pbis/bin/lwsm' shutdown

    if [ -f "/etc/init.d/lwsmd" ]; then
        run rm -f '/etc/init.d/lwsmd'
    fi

    if [ -f /etc/redhat-release ]; then
	if [ ! -f /usr/bin/systemctl ]; then
            run ln -s '/etc/pbis/redhat/lwsmd' '/etc/init.d/lwsmd'
	fi
    else
        run ln -s '/etc/pbis/suse/lwsmd' '/etc/init.d/lwsmd'
    fi

    remove_old_init_symlinks

    if [ -f /usr/bin/systemctl ]; then
	run /usr/bin/systemctl enable '/etc/pbis/redhat/lwsmd.service'
    else
        run /sbin/chkconfig --add lwsmd
    fi


# CA-206905: PBIS service started when it shouldn't be
# The migration will taken by xenserver-firstboot.git/firstboot.d/60-upgrade-likewise-to-pbis
# However, CA-261195 shows we need to start if this is an upgrade not a fresh install
# CA-338602, In upgrade case, we only start lwsmd when the domain is joined
determine_join_status
if [[ ( $1 -gt 1 ) && ( -n "$result" ) ]]; then
    if [ -x /sbin/service ]
    then
        run /sbin/service lwsmd start
    else
        run /usr/bin/systemctl start lwsmd
    fi
fi

# We never want to enable pam etc, as we don't use this config, instead we do it ourselves.
# See CA-211425 / CA-261195 for more details
if false; then
    determine_join_status
    if [ -n "$result" ]; then
        if [ -x '/opt/pbis/bin/domainjoin-cli' ]; then
            run '/opt/pbis/bin/domainjoin-cli' configure --enable pam
            run '/opt/pbis/bin/domainjoin-cli' configure --enable nsswitch
        fi
    else
        if [ -x '/opt/pbis/bin/domainjoin-cli' ]; then
            LOAD_ORDER=`/opt/pbis/bin/regshell list_values '[HKEY_THIS_MACHINE\Services\lsass\Parameters\Providers]' |grep 'LoadOrder.*Local'`
            if [ -n "${LOAD_ORDER}" ]; then

                run '/opt/pbis/bin/domainjoin-cli' configure --enable pam
                run '/opt/pbis/bin/domainjoin-cli' configure --enable nsswitch
            fi
        fi
    fi
fi

    run_quiet mv /var/lib/likewise /var/lib/likewise.old
    run_quiet rm -rf "${UPGRADEDIR}"

    execute_auxiliary_scripts

    symlink_pam_lsass
    
    logfile "Package: PowerBroker Identity Services Open postinstall finished"
}

echo "Pre postinstall"
postinstall $1
# Disable and re-enable the service to update the [install] section of the service
/usr/bin/systemctl --quiet disable upgrade-likewise-to-pbis.service || :
/usr/bin/systemctl --quiet disable lwsmd.service || :
/usr/bin/systemctl --quiet enable /etc/pbis/redhat/lwsmd.service || :
echo "Post postinstall"

%pre
DAEMONS_TO_HALT="lwsmd lwregd netlogond lwiod dcerpcd eventlogd lsassd reapsysld"

UPGRADEDIR=/var/lib/pbis-upgrade

LOG=/var/log/pbis-open-install.log

PKG_ARCH="__PKG_ARCH"

# Display to screen and log file with a blank line between entries.
log()
{
    echo $@
    echo
    echo $@ >> $LOG
    echo >> $LOG
}

# Display to screen and log file with no blank line.
_log()
{
    echo $@
    echo $@ >> $LOG
}

# Display to file.
logfile()
{
    echo $@ >> $LOG
    echo >> $LOG
}

# Execute command.
# If successful, note in log file.
# If not successful, note on screen and log file.
run()
{
    tlog=$("$@" 2>&1)
    err=$?
    if [ $err -eq 0 ]; then
        echo "Success: $@" >> $LOG
        echo "$tlog" >> $LOG
        echo >> $LOG
    else
        _log "Error: $@ returned $err"
        _log "$tlog"
        _log
    fi
    return $err
}

# Execute command.
# Log only to file.
run_quiet()
{
    tlog=$("$@" 2>&1)
    err=$?
    if [ $err -eq 0 ]; then
        echo "Success: $@" >> $LOG
    else
        echo "Error: $@ returned $err  (ignoring and continuing)" >> $LOG
    fi
    echo "$tlog" >> $LOG
    echo >> $LOG
    return $err
}

# Execute command.
# If successful, note in log file.
# If not successful, note on screen and log file and then exit.
run_or_fail()
{
    tlog=$("$@" 2>&1)
    err=$?
    if [ $err -eq 0 ]; then
        echo "Success: $@" >> $LOG
        echo "$tlog" >> $LOG
        echo >> $LOG
    else
        _log "Error: $@ returned $err  (aborting this script)"
        _log "$tlog"
        _log
        exit 1
    fi
    return $err
}

pre_upgrade()
{
    logfile "Package: PowerBroker Identity Services Open [pre upgrade] begins (`date`)"

    # CA-261195 We never enable the full pam configuration for pbis, as we don't
    # need it, as such we shouldn't need to disable it. Doing so requires us to
    # re-enable it, and re-enabling it in its entirety brings about CA-211425.
    # We could in theory safely disable and re-enable nsswitch, but as all the
    # logic to do the --enable is block disabled in this file (instead relying
    # on a first boot script), it's  simplest just to refuse to disable it here.
    # run_quiet '/opt/pbis/bin/domainjoin-cli' configure --disable pam
    # run_quiet '/opt/pbis/bin/domainjoin-cli' configure --disable nsswitch

    if [ -x /sbin/service ]
    then
        run_quiet /sbin/service lwsmd stop
    else
        run_quiet /etc/init.d/lwsmd stop
    fi

    for daemon in $DAEMONS_TO_HALT
    do
        run_quiet pkill -KILL -x $daemon
    done

    logfile "Package: PowerBroker Identity Services Open [pre upgrade] finished"
}

pre_install()
{
    logfile "Package: PowerBroker Identity Services Open [pre install] begins (`date`)"

    if [ -x /sbin/service ]
    then
        run_quiet /sbin/service lwsmd stop
    else
        run_quiet /etc/init.d/lwsmd stop
    fi

    for daemon in $DAEMONS_TO_HALT
    do
        run_quiet pkill -KILL -x $daemon
    done

    logfile "Package: PowerBroker Identity Services Open [pre install] finished"
    exit 0
}

if [ $1 -eq 1 ]; then
    pre_install
else
    pre_upgrade
    pre_install
fi

%preun
%systemd_preun upgrade-likewise-to-pbis.service

DAEMONS_TO_HALT="lwsmd lwregd netlogond lwiod dcerpcd eventlogd lsassd reapsysld"

UPGRADEDIR=/var/lib/pbis-upgrade

LOG=/var/log/pbis-open-install.log

PKG_ARCH="__PKG_ARCH"

# Display to screen and log file with a blank line between entries.
log()
{
    echo $@
    echo
    echo $@ >> $LOG
    echo >> $LOG
}

# Display to screen and log file with no blank line.
_log()
{
    echo $@
    echo $@ >> $LOG
}

# Display to file.
logfile()
{
    echo $@ >> $LOG
    echo >> $LOG
}

# Execute command.
# If successful, note in log file.
# If not successful, note on screen and log file.
run()
{
    tlog=$("$@" 2>&1)
    err=$?
    if [ $err -eq 0 ]; then
        echo "Success: $@" >> $LOG
        echo "$tlog" >> $LOG
        echo >> $LOG
    else
        _log "Error: $@ returned $err"
        _log "$tlog"
        _log
    fi
    return $err
}

# Execute command.
# Log only to file.
run_quiet()
{
    tlog=$("$@" 2>&1)
    err=$?
    if [ $err -eq 0 ]; then
        echo "Success: $@" >> $LOG
    else
        echo "Error: $@ returned $err  (ignoring and continuing)" >> $LOG
    fi
    echo "$tlog" >> $LOG
    echo >> $LOG
    return $err
}

# Execute command.
# If successful, note in log file.
# If not successful, note on screen and log file and then exit.
run_or_fail()
{
    tlog=$("$@" 2>&1)
    err=$?
    if [ $err -eq 0 ]; then
        echo "Success: $@" >> $LOG
        echo "$tlog" >> $LOG
        echo >> $LOG
    else
        _log "Error: $@ returned $err  (aborting this script)"
        _log "$tlog"
        _log
        exit 1
    fi
    return $err
}

execute_auxiliary_scripts()
{
    if [ -d "/var/lib/pbis/scripts/uninstall" ]; then
        for file in /var/lib/pbis/scripts/uninstall/*; do
            run_quiet "$file" --uninstall
        done
    fi
}

preuninstall_remove()
{
    logfile "Package: PowerBroker Identity Services Open [preun remove] begins (`date`)"

    execute_auxiliary_scripts

    run_quiet '/opt/pbis/bin/domainjoin-cli' configure --disable pam
    run_quiet '/opt/pbis/bin/domainjoin-cli' configure --disable nsswitch

    if [ -x /sbin/service ]
    then
        run_quiet /sbin/service lwsmd stop
    else
        run_quiet '/etc/init.d/lwsmd' stop
    fi

    for daemon in $DAEMONS_TO_HALT
    do
        run_quiet pkill -KILL -x $daemon
    done

    run_quiet /sbin/chkconfig --del lwsmd

    run_quiet rm -f '/etc/init.d/lwsmd'

    logfile "Package: PowerBroker Identity Services Open [preun remove] finished"
    exit 0
}

if [ $1 -eq 0 ]; then
    preuninstall_remove
fi
exit 0

%postun
%systemd_postun upgrade-likewise-to-pbis.service

%files 
%defattr(-,root,root)
/opt/pbis/bin/kinit
/opt/pbis/bin/klist
/opt/pbis/bin/kdestroy
/opt/pbis/bin/kvno
/opt/pbis/bin/ktutil
/opt/pbis/lib/krb5/plugins/preauth/pkinit.so
/opt/pbis/lib/libcom_err.so.3.0
/opt/pbis/lib/libcom_err.so.3
/opt/pbis/lib/libk5crypto.so.3.1
/opt/pbis/lib/libk5crypto.so.3
/opt/pbis/lib/libgssapi_krb5.so.2.2
/opt/pbis/lib/libgssapi_krb5.so.2
/opt/pbis/lib/libkrb5.so.3.3
/opt/pbis/lib/libkrb5.so.3
/opt/pbis/lib/libkadm5srv_mit.so.8.0
/opt/pbis/lib/libkadm5srv_mit.so.8
/opt/pbis/lib/libkdb5.so.5.0
/opt/pbis/lib/libkdb5.so.5
/opt/pbis/lib/libgssrpc.so.4.1
/opt/pbis/lib/libgssrpc.so.4
/opt/pbis/lib/libkrb5support.so.0.1
/opt/pbis/lib/libkrb5support.so.0
/opt/pbis/lib/sasl2/libgssapiv2.so.2.0.23
/opt/pbis/lib/sasl2/libgssapiv2.so.2
/opt/pbis/lib/sasl2/libgssapiv2.so
/opt/pbis/lib/sasl2/libgssspnego.so.2.0.23
/opt/pbis/lib/sasl2/libgssspnego.so.2
/opt/pbis/lib/sasl2/libgssspnego.so
/opt/pbis/lib/libsasl2.so.2.0.23
/opt/pbis/lib/libsasl2.so.2
/opt/pbis/lib/libldap-2.4.so.2.4.2
/opt/pbis/lib/libldap-2.4.so.2
/opt/pbis/lib/liblber-2.4.so.2.4.2
/opt/pbis/lib/liblber-2.4.so.2
/opt/pbis/lib/libldap_r-2.4.so.2.4.2
/opt/pbis/lib/libldap_r-2.4.so.2
/opt/pbis/bin/ldapsearch
/opt/pbis/bin/sqlite3
/opt/pbis/lib/libsqlite3.so.0.8.6
/opt/pbis/lib/libsqlite3.so.0
/opt/pbis/lib/libtdb.so.0.0.0
/opt/pbis/lib/libtdb.so.0
/opt/pbis/lib/liblwbase_nothr.so.0.0.0
/opt/pbis/lib/liblwbase_nothr.so.0
/opt/pbis/lib/liblwbase.so.0.0.0
/opt/pbis/lib/liblwbase.so.0
/opt/pbis/sbin/lw-svcm-wrap
/opt/pbis/docs/html/lwbase
/opt/pbis/lib/liblwmsg_nothr.so.0.0.0
/opt/pbis/lib/liblwmsg_nothr.so.0
/opt/pbis/lib/liblwmsg.so.0.0.0
/opt/pbis/lib/liblwmsg.so.0
/opt/pbis/libexec/lwma
/opt/pbis/docs/html/lwmsg
/opt/pbis/lib/libregcommon.so.0.0.0
/opt/pbis/lib/libregcommon.so.0
/opt/pbis/lib/libregclient.so.0.0.0
/opt/pbis/lib/libregclient.so.0
/opt/pbis/lib/librsutils.so.0.0.0
/opt/pbis/lib/librsutils.so.0
/opt/pbis/lib/lw-svcm/lwreg-sqlite.so
/opt/pbis/lib/lw-svcm/lwreg-memory.so
/opt/pbis/lib/lw-svcm/lwreg.so
/opt/pbis/share/config/lwreg.reg
/opt/pbis/bin/regshell
/opt/pbis/bin/edit-reg
/opt/pbis/lib/liblwadvapi.so.0.0.0
/opt/pbis/lib/liblwadvapi.so.0
/opt/pbis/lib/liblwadvapi_nothr.so.0.0.0
/opt/pbis/lib/liblwadvapi_nothr.so.0
/opt/pbis/lib/liblwnetcommon.so.0.0.0
/opt/pbis/lib/liblwnetcommon.so.0
/opt/pbis/lib/liblwnetclientapi.so.0.0.0
/opt/pbis/lib/liblwnetclientapi.so.0
/opt/pbis/lib/lw-svcm/netlogon.so
/opt/pbis/lib/krb5/plugins/libkrb5/liblwnet_service_locator.so
/opt/pbis/bin/get-dc-name
/opt/pbis/bin/get-dc-list
/opt/pbis/bin/get-dc-time
/opt/pbis/share/config/netlogond.reg
/opt/pbis/lib/liblwiocommon.so.0.0.0
/opt/pbis/lib/liblwiocommon.so.0
/opt/pbis/lib/liblwioshareinfo.so.0.0.0
/opt/pbis/lib/liblwioshareinfo.so.0
/opt/pbis/lib/liblwioclient.so.0.0.0
/opt/pbis/lib/liblwioclient.so.0
/opt/pbis/lib/libiomgr.so.0.0.0
/opt/pbis/lib/libiomgr.so.0
/opt/pbis/lib/liblwiosmbcommon.so.0.0.0
/opt/pbis/lib/liblwiosmbcommon.so.0
/opt/pbis/lib/lwio-driver/rdr.so
/opt/pbis/lib/lw-svcm/lwio.so
/opt/pbis/lib/libiotest.sys.so
/opt/pbis/bin/lwio-driver
/opt/pbis/bin/lwio-copy
/opt/pbis/share/config/lwiod.reg
/opt/pbis/share/config/rdr.reg
/opt/pbis/lib/libschannel.so.0.0.0
/opt/pbis/lib/libschannel.so.0
/opt/pbis/lib/libdcerpc.so.1.2.0
/opt/pbis/lib/libdcerpc.so.1
/opt/pbis/lib/lw-svcm/dcerpc.so
/opt/pbis/share/config/dcerpcd.reg
/opt/pbis/lib/libcentutils.so.0.0.0
/opt/pbis/lib/libcentutils.so.0
/opt/pbis/lib/liblwsmcommon.so.0.0.0
/opt/pbis/lib/liblwsmcommon.so.0
/opt/pbis/lib/liblwsm.so.0.0.0
/opt/pbis/lib/liblwsm.so.0
/opt/pbis/bin/lwsm
/opt/pbis/sbin/lwsmd
/opt/pbis/docs/html/lwsm
/opt/pbis/lib/libadtool.so.0.0.0
/opt/pbis/lib/libadtool.so.0
/opt/pbis/bin/adtool
/opt/pbis/lib/libeventlogutils.so.0.0.0
/opt/pbis/lib/libeventlogutils.so.0
/opt/pbis/lib/libeventlog.so.0.0.0
/opt/pbis/lib/libeventlog.so.0
/opt/pbis/lib/libeventlog_norpc.so.0.0.0
/opt/pbis/lib/libeventlog_norpc.so.0
/opt/pbis/lib/lw-svcm/eventlog.so
/opt/pbis/bin/eventlog-cli
/opt/pbis/share/config/eventlogd.reg
/opt/pbis/lib/liblsacommon.so.0.0.0
/opt/pbis/lib/liblsacommon.so.0
/opt/pbis/lib/liblsapstore.so.0.0.0
/opt/pbis/lib/liblsapstore.so.0
/opt/pbis/lib/liblsaclient.so.0.0.0
/opt/pbis/lib/liblsaclient.so.0
/opt/pbis/lib/liblsaclientthr.so.0.0.0
/opt/pbis/lib/liblsaclientthr.so.0
/opt/pbis/lib/liblsaclient_ntlm.so.0.0.0
/opt/pbis/lib/liblsaclient_ntlm.so.0
/opt/pbis/lib/liblsarpc.so.0.0.0
/opt/pbis/lib/liblsarpc.so.0
/opt/pbis/lib/liblsaauth.so.0.0.0
/opt/pbis/lib/liblsaauth.so.0
/opt/pbis/lib/lw-map-sec/lsass.so
/opt/pbis/lib/gss/libgssapi_ntlm.so
/opt/pbis/lib/liblsagsswrap.so.0.0.0
/opt/pbis/lib/liblsagsswrap.so.0
/opt/pbis/lib/liblsaserverapi.so.0.0.0
/opt/pbis/lib/liblsaserverapi.so.0
/opt/pbis/lib/libntlmserver.so.0.0.0
/opt/pbis/lib/libntlmserver.so.0
/opt/pbis/lib/libdsapi.so.0.0.0
/opt/pbis/lib/libdsapi.so.0
/opt/pbis/lib/lsa-provider/local.so
/opt/pbis/lib/lsa-provider/ad_open.so
/opt/pbis/lib/lsa-rpc/samr.so
/opt/pbis/lib/lsa-rpc/lsa.so
/opt/pbis/lib/lsa-rpc/dssetup.so
/opt/pbis/lib/lsa-rpc/wkssvc.so
/opt/pbis/lib/lw-svcm/lsass.so
/opt/pbis/bin/lsa
/opt/pbis/bin/ad-cache
/opt/pbis/bin/add-group
/opt/pbis/bin/add-user
/opt/pbis/bin/del-group
/opt/pbis/bin/del-user
/opt/pbis/bin/enum-groups
/opt/pbis/bin/enum-users
/opt/pbis/bin/find-by-sid
/opt/pbis/bin/find-group-by-id
/opt/pbis/bin/find-group-by-name
/opt/pbis/bin/find-user-by-id
/opt/pbis/bin/find-user-by-name
/opt/pbis/bin/get-metrics
/opt/pbis/bin/get-status
/opt/pbis/bin/pbis-status
/opt/pbis/bin/list-groups-for-user
/opt/pbis/bin/ypcat
/opt/pbis/bin/ypmatch
/opt/pbis/bin/mod-group
/opt/pbis/bin/mod-user
/opt/pbis/bin/find-objects
/opt/pbis/bin/enum-objects
/opt/pbis/bin/enum-members
/opt/pbis/bin/query-member-of
/opt/pbis/bin/passwd
/opt/pbis/share/config/lsassd.reg
/opt/pbis/share/config/privileges.reg
/opt/pbis/share/config/accounts.reg
/opt/pbis/docs/html/lsass
/opt/pbis/lib/liblwdns.so.0.0.0
/opt/pbis/lib/liblwdns.so.0
/opt/pbis/bin/update-dns
/opt/pbis/lib/liblwnetapi.so.0.0.0
/opt/pbis/lib/liblwnetapi.so.0
/opt/pbis/lib/libOpenSOAPClient.so.2.0.0
/opt/pbis/lib/libOpenSOAPClient.so.2
/opt/pbis/lib/libOpenSOAPSecurity.so.2.0.0
/opt/pbis/lib/libOpenSOAPSecurity.so.2
/opt/pbis/lib/libOpenSOAPService.so.2.0.0
/opt/pbis/lib/libOpenSOAPService.so.2
/opt/pbis/lib/libdomainjoin.so.0.0.0
/opt/pbis/lib/libdomainjoin.so.0
/opt/pbis/bin/domainjoin-cli
/opt/pbis/libexec/ConfigureLogin
/opt/pbis/libexec/gpcron
/opt/pbis/bin/config
/opt/pbis/libexec/conf2reg
/opt/pbis/libexec/regupgr61.sh
/opt/pbis/libexec/reg61sed.sh
/opt/pbis/lib/libwbclient.so.0.0.0
/opt/pbis/lib/libwbclient.so.0
/opt/pbis/lib/lwicompat_v4.so
/opt/pbis/lib/lw-pstore/samba.so
/opt/pbis/bin/samba-interop-install
/opt/pbis/libexec/init-base.sh
/opt/pbis/data/VERSION
/opt/pbis/bin/uninstall.sh
/opt/pbis/share/pbis.pam-auth-update
/opt/pbis/share/rhel/7.0/pbis.te
/opt/pbis/share/rhel/7.0/pbis.fc
/opt/pbis/share/rhel/7.0/pbis.if
/opt/pbis/share/rhel/7.0/pbis.pp
/opt/pbis/share/rhel/6.0/pbis.te
/opt/pbis/share/rhel/6.0/pbis.fc
/opt/pbis/share/rhel/6.0/pbis.if
/opt/pbis/share/rhel/6.0/pbis.pp
/opt/pbis/share/fedora/20/pbis.te
/opt/pbis/share/fedora/20/pbis.fc
/opt/pbis/share/fedora/20/pbis.if
/opt/pbis/share/fedora/20/pbis.pp
/opt/pbis/share/fedora/19/pbis.te
/opt/pbis/share/fedora/19/pbis.fc
/opt/pbis/share/fedora/19/pbis.if
/opt/pbis/share/fedora/19/pbis.pp
/opt/pbis/share/fedora/18/pbis.te
/opt/pbis/share/fedora/18/pbis.fc
/opt/pbis/share/fedora/18/pbis.if
/opt/pbis/share/fedora/18/pbis.pp
/opt/pbis/share/fedora/17/pbis.te
/opt/pbis/share/fedora/17/pbis.fc
/opt/pbis/share/fedora/17/pbis.if
/opt/pbis/share/fedora/17/pbis.pp
/opt/pbis/share/fedora/16/pbis.te
/opt/pbis/share/fedora/16/pbis.fc
/opt/pbis/share/fedora/16/pbis.if
/opt/pbis/share/fedora/16/pbis.pp
/opt/pbis/share/fedora/15/pbis.te
/opt/pbis/share/fedora/15/pbis.fc
/opt/pbis/share/fedora/15/pbis.if
/opt/pbis/share/fedora/15/pbis.pp
/opt/pbis/share/fedora/14/pbis.te
/opt/pbis/share/fedora/14/pbis.fc
/opt/pbis/share/fedora/14/pbis.if
/opt/pbis/share/fedora/14/pbis.pp
/opt/pbis/share/fedora/13/pbis.te
/opt/pbis/share/fedora/13/pbis.fc
/opt/pbis/share/fedora/13/pbis.if
/opt/pbis/share/fedora/13/pbis.pp
/opt/pbis/libexec/pbis-support.pl
/opt/pbis/libexec/upgrade-likewise-to-pbis
/opt/pbis/docs/pbis-open-installation-and-administration-guide.pdf
/opt/pbis/docs/pbis-quick-start-guide-for-linux.pdf
/opt/pbis/lib/krb5/plugins/preauth/pacreq.so
/lib/security/pam_lsass.so
/lib/security/pam_lsass.la
/lib/libnss_lsass.so.2
/lib/libnss_lsass.la
/usr/bin/pbis
/usr/bin/domainjoin-cli
/etc/pbis/pbis-krb5-ad.conf
/var/lib/pbis/lwreport.xml
/etc/pbis/gss/mech
/etc/pbis/user-ignore
/etc/pbis/group-ignore
/var/lib/pbis/lwconfig.xml
/etc/pbis/debian/lwsmd
/etc/pbis/redhat/lwsmd
/etc/pbis/redhat/lwsmd.service
/etc/pbis/suse/lwsmd
%{_unitdir}/upgrade-likewise-to-pbis.service
%dir /var/lib/pbis
%dir /var/lib/pbis/rpc

%files devel
%defattr(-,root,root)
/opt/pbis/include/krb5/krb5.h
/opt/pbis/include/krb5/locate_plugin.h
/opt/pbis/include/krb5/preauth_plugin.h
/opt/pbis/include/kdb.h
/opt/pbis/include/krb5.h
/opt/pbis/include/gssapi/gssapi_err_generic.h
/opt/pbis/include/gssapi/mechglue.h
/opt/pbis/include/gssapi/gssapi_ext.h
/opt/pbis/include/gssapi/gssapi_krb5.h
/opt/pbis/include/gssapi/gssapi_generic.h
/opt/pbis/include/gssapi/gssapi.h
/opt/pbis/include/profile.h
/opt/pbis/include/com_err.h
/opt/pbis/include/gssapi.h
/opt/pbis/include/sasl/md5global.h
/opt/pbis/include/sasl/sasl.h
/opt/pbis/include/sasl/hmac-md5.h
/opt/pbis/include/sasl/saslplug.h
/opt/pbis/include/sasl/md5.h
/opt/pbis/include/sasl/prop.h
/opt/pbis/include/sasl/saslutil.h
/opt/pbis/include/ldap_cdefs.h
/opt/pbis/include/lber_types.h
/opt/pbis/include/lber.h
/opt/pbis/include/slapi-plugin.h
/opt/pbis/include/ldap.h
/opt/pbis/include/ldap_utf8.h
/opt/pbis/include/ldap_features.h
/opt/pbis/include/ldap_schema.h
/opt/pbis/include/sqlite3.h
/opt/pbis/include/sqlite3ext.h
/opt/pbis/include/tdb.h
/opt/pbis/include/tchar.h
/opt/pbis/include/wchar16.h
/opt/pbis/include/wc16str.h
/opt/pbis/include/wc16printf.h
/opt/pbis/include/lwprintf.h
/opt/pbis/include/lw/dscache.h
/opt/pbis/include/lw/errno.h
/opt/pbis/include/lw/ntstatus.h
/opt/pbis/include/lw/winerror.h
/opt/pbis/include/lw/rpcstatus.h
/opt/pbis/include/lw/types.h
/opt/pbis/include/lw/attrs.h
/opt/pbis/include/lw/atomic.h
/opt/pbis/include/lw/hash.h
/opt/pbis/include/lw/rtllog.h
/opt/pbis/include/lw/rtlmemory.h
/opt/pbis/include/lw/rtlstring.h
/opt/pbis/include/lw/rtlgoto.h
/opt/pbis/include/lw/rbtree.h
/opt/pbis/include/lw/swab.h
/opt/pbis/include/lw/safeint.h
/opt/pbis/include/lw/security-types.h
/opt/pbis/include/lw/security-api.h
/opt/pbis/include/lw/threadpool.h
/opt/pbis/include/lw/affinity.h
/opt/pbis/include/lw/mapsecurity.h
/opt/pbis/include/lw/mapsecurity-types.h
/opt/pbis/include/lw/mapsecurity-plugin.h
/opt/pbis/include/lw/svcm.h
/opt/pbis/include/lw/base.h
/opt/pbis/include/lwmsg/call.h
/opt/pbis/include/lwmsg/message.h
/opt/pbis/include/lwmsg/data.h
/opt/pbis/include/lwmsg/assoc.h
/opt/pbis/include/lwmsg/context.h
/opt/pbis/include/lwmsg/time.h
/opt/pbis/include/lwmsg/buffer.h
/opt/pbis/include/lwmsg/connection.h
/opt/pbis/include/lwmsg/protocol.h
/opt/pbis/include/lwmsg/status.h
/opt/pbis/include/lwmsg/type.h
/opt/pbis/include/lwmsg/peer.h
/opt/pbis/include/lwmsg/security.h
/opt/pbis/include/lwmsg/common.h
/opt/pbis/include/lwmsg/session.h
/opt/pbis/include/lwmsg/archive.h
/opt/pbis/include/lwmsg/lwmsg.h
/opt/pbis/include/reg/lwntreg.h
/opt/pbis/include/reg/reg.h
/opt/pbis/include/reg/lwreg.h
/opt/pbis/include/reg/regutil.h
/opt/pbis/include/lwdef.h
/opt/pbis/include/lwerror.h
/opt/pbis/include/lwfile.h
/opt/pbis/include/lwkrb5.h
/opt/pbis/include/lwldap.h
/opt/pbis/include/lwmem.h
/opt/pbis/include/lwsecurityidentifier.h
/opt/pbis/include/lwstr.h
/opt/pbis/include/lwtime.h
/opt/pbis/include/lwsid.h
/opt/pbis/include/lwldap-error.h
/opt/pbis/include/lwdscache.h
/opt/pbis/include/lwhash.h
/opt/pbis/include/lwbuffer.h
/opt/pbis/include/lwdlinked-list.h
/opt/pbis/include/lwadvapi.h
/opt/pbis/include/lwnet.h
/opt/pbis/include/lwnet-plugin.h
/opt/pbis/include/lwio/io-types.h
/opt/pbis/include/lwio/io-types-posix.h
/opt/pbis/include/lwio/iortl.h
/opt/pbis/include/lwio/ntfileapi.h
/opt/pbis/include/lwio/smbfileapi.h
/opt/pbis/include/lwio/srvshareapi.h
/opt/pbis/include/lwio/srvtransportapi.h
/opt/pbis/include/lwio/lmfile.h
/opt/pbis/include/lwio/lmsession.h
/opt/pbis/include/lwio/lmshare.h
/opt/pbis/include/lwio/lmconnection.h
/opt/pbis/include/lwio/lwconnectioninfo.h
/opt/pbis/include/lwio/lwfileinfo.h
/opt/pbis/include/lwio/lwiofsctl.h
/opt/pbis/include/lwio/lwiodevctl.h
/opt/pbis/include/lwio/lwsessioninfo.h
/opt/pbis/include/lwio/lwshareinfo.h
/opt/pbis/include/lwio/iodriver.h
/opt/pbis/include/lwio/ioapi.h
/opt/pbis/include/lwio/lwzct.h
/opt/pbis/include/lwio/lwio.h
/opt/pbis/include/schtypes.h
/opt/pbis/include/schannel.h
/opt/pbis/include/dce/codesets_stub.h
/opt/pbis/include/dce/stubbase.h
/opt/pbis/include/dce/idl_es.h
/opt/pbis/include/dce/idlbase.h
/opt/pbis/include/dce/idlddefs.h
/opt/pbis/include/dce/rpcexc.h
/opt/pbis/include/dce/dce_utils.h
/opt/pbis/include/dce/sec_authn.h
/opt/pbis/include/dce/dce.h
/opt/pbis/include/dce/dce_error.h
/opt/pbis/include/dce/marshall.h
/opt/pbis/include/dce/ndr_rep.h
/opt/pbis/include/dce/ndrtypes.h
/opt/pbis/include/dce/dcethread.h
/opt/pbis/include/dce/linux-gnu/dce_error.h
/opt/pbis/include/dce/linux-gnu/dce.h
/opt/pbis/include/dce/x86_64/ndrtypes.h
/opt/pbis/include/dce/x86_64/ndr_rep.h
/opt/pbis/include/dce/x86_64/marshall.h
/opt/pbis/include/dce/codesets.h
/opt/pbis/include/dce/conv.h
/opt/pbis/include/dce/convc.h
/opt/pbis/include/dce/ep.h
/opt/pbis/include/dce/iovector.h
/opt/pbis/include/dce/lbase.h
/opt/pbis/include/dce/mgmt.h
/opt/pbis/include/dce/nbase.h
/opt/pbis/include/dce/ncastat.h
/opt/pbis/include/dce/ndrold.h
/opt/pbis/include/dce/rpcbase.h
/opt/pbis/include/dce/rpcpvt.h
/opt/pbis/include/dce/rpcsts.h
/opt/pbis/include/dce/rpctypes.h
/opt/pbis/include/dce/twr.h
/opt/pbis/include/dce/uuid.h
/opt/pbis/include/dce/id_base.h
/opt/pbis/include/dce/schannel.h
/opt/pbis/include/dce/smb.h
/opt/pbis/include/dce/lrpc.h
/opt/pbis/include/dce/rpc.h
/opt/pbis/include/dce/codesets.idl
/opt/pbis/include/dce/conv.idl
/opt/pbis/include/dce/convc.idl
/opt/pbis/include/dce/ep.idl
/opt/pbis/include/dce/iovector.idl
/opt/pbis/include/dce/lbase.idl
/opt/pbis/include/dce/mgmt.idl
/opt/pbis/include/dce/nbase.idl
/opt/pbis/include/dce/ncastat.idl
/opt/pbis/include/dce/ndrold.idl
/opt/pbis/include/dce/rpc.idl
/opt/pbis/include/dce/rpcbase.idl
/opt/pbis/include/dce/rpcpvt.idl
/opt/pbis/include/dce/rpcsts.idl
/opt/pbis/include/dce/rpctypes.idl
/opt/pbis/include/dce/twr.idl
/opt/pbis/include/dce/uuid.idl
/opt/pbis/include/dce/id_base.idl
/opt/pbis/include/compat/rpcfields.h
/opt/pbis/include/compat/baserpc.h
/opt/pbis/include/compat/dce2msrpc.h
/opt/pbis/include/compat/dcerpc.h
/opt/pbis/include/lwrpcrt/lwrpcrt.h
/opt/pbis/include/ctarray.h
/opt/pbis/include/ctdef.h
/opt/pbis/include/ctexec.h
/opt/pbis/include/ctfileutils.h
/opt/pbis/include/cthash.h
/opt/pbis/include/ctmem.h
/opt/pbis/include/ctprocutils.h
/opt/pbis/include/ctrwlock.h
/opt/pbis/include/ctshell.h
/opt/pbis/include/ctstrutils.h
/opt/pbis/include/ctsys.h
/opt/pbis/include/cttext.h
/opt/pbis/include/ctuser.h
/opt/pbis/include/lwexc.h
/opt/pbis/include/ctsysfuncs.h
/opt/pbis/include/ctbase.h
/opt/pbis/include/lwsm/lwsm.h
/opt/pbis/include/adtool/types.h
/opt/pbis/include/eventlog.h
/opt/pbis/include/eventlog-record.h
/opt/pbis/include/lsa/provider.h
/opt/pbis/include/lsa/lsa.h
/opt/pbis/include/lsa/lsapstore-types.h
/opt/pbis/include/lsa/lsapstore-plugin.h
/opt/pbis/include/lsa/lsapstore-api.h
/opt/pbis/include/lsa/ad-types.h
/opt/pbis/include/lsa/ad.h
/opt/pbis/include/lsa/privilege.h
/opt/pbis/include/ntlm/gssntlm.h
/opt/pbis/include/ntlm/sspintlm.h
/opt/pbis/include/lw/rpc/common.h
/opt/pbis/include/lw/rpc/lsa.h
/opt/pbis/include/lw/rpc/samr.h
/opt/pbis/include/lw/rpc/netlogon.h
/opt/pbis/include/lw/rpc/dssetup.h
/opt/pbis/include/lw/rpc/krb5pac.h
/opt/pbis/include/lw/rpc/wkssvc.h
/opt/pbis/include/lsa/internal/lsaadprovider.h
/opt/pbis/include/lsa/internal/lsalocalprovider.h
/opt/pbis/include/lsa/internal/lsadatablob.h
/opt/pbis/include/lsa/internal/lsadef.h
/opt/pbis/include/lsa/internal/lsaipc-common.h
/opt/pbis/include/lsa/internal/lsaipc.h
/opt/pbis/include/lsa/internal/lsaipc-privilege.h
/opt/pbis/include/lsa/internal/lsaprivilege-internal.h
/opt/pbis/include/lsa/internal/lsalist.h
/opt/pbis/include/lsa/internal/lsasrvcred.h
/opt/pbis/include/lsa/internal/lsasystem.h
/opt/pbis/include/lsa/internal/lsautils.h
/opt/pbis/include/lsa/internal/lwsecurityidentifier.h
/opt/pbis/include/lsa/internal/machinepwdinfo-impl.h
/opt/pbis/include/lsa/internal/xpg_socket.h
/opt/pbis/include/lsa/internal/lsasrvapi.h
/opt/pbis/include/lsa/internal/lsasrvutils.h
/opt/pbis/include/lwdns.h
/opt/pbis/include/lw/lmaccess.h
/opt/pbis/include/lw/lmcreds.h
/opt/pbis/include/lw/lmcrypt.h
/opt/pbis/include/lw/lmdebug.h
/opt/pbis/include/lw/lmerr.h
/opt/pbis/include/lw/lmjoin.h
/opt/pbis/include/lw/lmmem.h
/opt/pbis/include/lw/lmshare.h
/opt/pbis/include/lw/lmwksta.h
/opt/pbis/include/lw/lmserver.h
/opt/pbis/include/lw/lm.h
/opt/pbis/include/OpenSOAP/Block.h
/opt/pbis/include/OpenSOAP/ByteArray.h
/opt/pbis/include/OpenSOAP/CStdio.h
/opt/pbis/include/OpenSOAP/ClientSocket.h
/opt/pbis/include/OpenSOAP/Defines.h
/opt/pbis/include/OpenSOAP/Envelope.h
/opt/pbis/include/OpenSOAP/ErrorCode.h
/opt/pbis/include/OpenSOAP/Locale.h
/opt/pbis/include/OpenSOAP/OpenSOAP.h
/opt/pbis/include/OpenSOAP/Serializer.h
/opt/pbis/include/OpenSOAP/Service.h
/opt/pbis/include/OpenSOAP/Security.h
/opt/pbis/include/OpenSOAP/Stream.h
/opt/pbis/include/OpenSOAP/String.h
/opt/pbis/include/OpenSOAP/StringHash.h
/opt/pbis/include/OpenSOAP/Transport.h
/opt/pbis/include/OpenSOAP/XMLAttr.h
/opt/pbis/include/OpenSOAP/XMLElm.h
/opt/pbis/include/OpenSOAP/XMLNamespace.h
/opt/pbis/include/djdistroinfo.h
/opt/pbis/lib/libcom_err.so
/opt/pbis/lib/libk5crypto.so
/opt/pbis/lib/libkadm5srv_mit.so
/opt/pbis/lib/libgssrpc.so
/opt/pbis/lib/libkrb5support.so
/opt/pbis/lib/libcom_err.la
/opt/pbis/lib/libk5crypto.la
/opt/pbis/lib/libgssapi_krb5.la
/opt/pbis/lib/libkrb5.la
/opt/pbis/lib/libkadm5srv_mit.la
/opt/pbis/lib/libkdb5.la
/opt/pbis/lib/libgssrpc.la
/opt/pbis/lib/libkrb5support.la
/opt/pbis/lib/libsasl2.la
/opt/pbis/lib/libldap.so
/opt/pbis/lib/libldap_r.so
/opt/pbis/lib/liblber.so
/opt/pbis/lib/libldap.la
/opt/pbis/lib/libldap_r.la
/opt/pbis/lib/liblber.la
/opt/pbis/lib/libsqlite3.la
/opt/pbis/lib/libtdb.so
/opt/pbis/lib/libtdb.la
/opt/pbis/lib/liblwbase_nothr.so
/opt/pbis/lib/liblwbase_nothr.la
/opt/pbis/lib/liblwbase.so
/opt/pbis/lib/liblwbase.la
/opt/pbis/lib/liblwmsg_nothr.so
/opt/pbis/lib/liblwmsg_nothr.la
/opt/pbis/lib/liblwmsg.so
/opt/pbis/lib/liblwmsg.la
/opt/pbis/lib/libregcommon.so
/opt/pbis/lib/libregcommon.la
/opt/pbis/lib/libregclient.so
/opt/pbis/lib/libregclient.la
/opt/pbis/lib/librsutils.so
/opt/pbis/lib/librsutils.la
/opt/pbis/lib/liblwadvapi.so
/opt/pbis/lib/liblwadvapi.la
/opt/pbis/lib/liblwadvapi_nothr.so
/opt/pbis/lib/liblwadvapi_nothr.la
/opt/pbis/lib/liblwnetcommon.so
/opt/pbis/lib/liblwnetcommon.la
/opt/pbis/lib/liblwnetclientapi.so
/opt/pbis/lib/liblwnetclientapi.la
/opt/pbis/lib/liblwiocommon.so
/opt/pbis/lib/liblwiocommon.la
/opt/pbis/lib/liblwioshareinfo.so
/opt/pbis/lib/liblwioshareinfo.la
/opt/pbis/lib/liblwioclient.so
/opt/pbis/lib/liblwioclient.la
/opt/pbis/lib/libiomgr.so
/opt/pbis/lib/libiomgr.la
/opt/pbis/lib/liblwiosmbcommon.so
/opt/pbis/lib/liblwiosmbcommon.la
/opt/pbis/lib/libiotest.sys.so
/opt/pbis/lib/libiotest.sys.la
/opt/pbis/lib/libschannel.so
/opt/pbis/lib/libschannel.la
/opt/pbis/lib/libdcerpc.so
/opt/pbis/lib/libdcerpc.la
/opt/pbis/lib/libcentutils.so
/opt/pbis/lib/libcentutils.la
/opt/pbis/lib/liblwsmcommon.so
/opt/pbis/lib/liblwsmcommon.la
/opt/pbis/lib/liblwsm.so
/opt/pbis/lib/liblwsm.la
/opt/pbis/lib/libadtool.so
/opt/pbis/lib/libadtool.la
/opt/pbis/lib/libeventlogutils.so
/opt/pbis/lib/libeventlogutils.la
/opt/pbis/lib/libeventlog.so
/opt/pbis/lib/libeventlog.la
/opt/pbis/lib/libeventlog_norpc.so
/opt/pbis/lib/libeventlog_norpc.la
/opt/pbis/lib/liblsacommon.so
/opt/pbis/lib/liblsacommon.la
/opt/pbis/lib/liblsapstore.so
/opt/pbis/lib/liblsapstore.la
/opt/pbis/lib/liblsaclient.so
/opt/pbis/lib/liblsaclient.la
/opt/pbis/lib/liblsaclientthr.so
/opt/pbis/lib/liblsaclientthr.la
/opt/pbis/lib/liblsaclient_ntlm.so
/opt/pbis/lib/liblsaclient_ntlm.la
/opt/pbis/lib/liblsarpc.so
/opt/pbis/lib/liblsarpc.la
/opt/pbis/lib/liblsaauth.so
/opt/pbis/lib/liblsaauth.la
/opt/pbis/lib/liblsagsswrap.so
/opt/pbis/lib/liblsagsswrap.la
/opt/pbis/lib/liblsaserverapi.so
/opt/pbis/lib/liblsaserverapi.la
/opt/pbis/lib/libntlmserver.so
/opt/pbis/lib/libntlmserver.la
/opt/pbis/lib/libdsapi.so
/opt/pbis/lib/libdsapi.la
/opt/pbis/lib/liblwdns.so
/opt/pbis/lib/liblwdns.la
/opt/pbis/lib/liblwnetapi.so
/opt/pbis/lib/liblwnetapi.la
/opt/pbis/lib/libOpenSOAPClient.so
/opt/pbis/lib/libOpenSOAPSecurity.so
/opt/pbis/lib/libOpenSOAPService.so
/opt/pbis/lib/libOpenSOAPClient.la
/opt/pbis/lib/libOpenSOAPSecurity.la
/opt/pbis/lib/libOpenSOAPService.la
/opt/pbis/lib/libdomainjoin.so
/opt/pbis/lib/libdomainjoin.la
/opt/pbis/lib/libwbclient.so
/opt/pbis/lib/libwbclient.la
/opt/pbis/lib/lwicompat_v4.la

%changelog
* Mon Jun 1 2020 Lin Liu <lin.liu@citrix.com> - 8.2.3-1.7.7
- CA-340470: Remove lwsmd from auto-start in upgrade case

* Tue Jan 21 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 8.2.3-1.7.5
- CP-31092: Move upgrade-likewise-to-pbis to its own service

* Fri Sep 20 2019 Deli Zhang <deli.zhang@citrix.com> - 8.2.3-1.7.4
- CA-324607: domainjoin-cli crashes for empty second-level domain

* Wed Oct 31 2018 Liang Dai <liang.dai1@citrix.com> - 8.2.2-1.7.3
- CA-291988: The pool failed to enable external authentication.

* Fri Jun 23 2017 Simon Rowe <simon.rowe@eu.citrix.com> - 8.2.2-1.5.0
- CA-257199: remove self-referencing Provides:
