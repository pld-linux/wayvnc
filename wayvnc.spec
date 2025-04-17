Summary:	A VNC server for wlroots based Wayland compositors
Name:		wayvnc
Version:	0.9.1
Release:	1
License:	ISC
Group:		Applications
Source0:	https://github.com/any1/wayvnc/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a24b8dc1e6fe1fd14ad9532d9dc6f0d6
URL:		https://github.com/any1/wayvnc
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	aml-devel < 0.4.0
BuildRequires:	aml-devel >= 0.3.0
BuildRequires:	jansson-devel
BuildRequires:	libdrm-devel
BuildRequires:	meson
BuildRequires:	neatvnc-devel < 0.10
BuildRequires:	neatvnc-devel >= 0.9
BuildRequires:	ninja
BuildRequires:	pam-devel
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc
BuildRequires:	wayland-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires:	aml-devel < 0.4.0
Requires:	aml-devel >= 0.3.0
Requires:	neatvnc-devel < 0.10
Requires:	neatvnc-devel >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VNC server for wlroots-based Wayland compositors (Gnome, KDE and
Weston are not supported). It attaches to a running Wayland session,
creates virtual input devices, and exposes a single display via the
RFB protocol. The Wayland session may be a headless one, so it is also
possible to run wayvnc without a physical display attached.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md COPYING FAQ.md README.md
%attr(755,root,root) %{_bindir}/wayvnc
%attr(755,root,root) %{_bindir}/wayvncctl
%{_mandir}/man1/wayvnc.1*
%{_mandir}/man1/wayvncctl.1*
