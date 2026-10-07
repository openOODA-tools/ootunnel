Name:           ootunnel
Version:        0.1.0
Release:        1%{?dist}
Summary:        Encrypted point-to-point WireGuard mesh tunnel establishing zero-trust paths.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootunnel
Source0:        ootunnel-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootunnel is a sovereign, capability-bounded ENCRYPTED TUNNEL written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootunnel
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootunnel-uninstall

%files
/usr/bin/ootunnel
/usr/bin/ootunnel-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
