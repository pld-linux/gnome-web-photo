Summary:	Tool to generate full-size image files and thumbnails
Summary(pl.UTF-8):	Narzędzie do generowania pełnowymiarowych plików obrazów i miniaturek
Name:		gnome-web-photo
Version:	0.3
Release:	8
License:	GPL
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-web-photo/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	1c9cdf4ce25b58641e0af16215c413a5
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-vfs2-devel >= 2.18.0
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	xulrunner-devel
Requires(post,preun):	GConf2
%requires_eq_to	xulrunner xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Web Photographer is a tool to generate full-size image files and
thumbnails from HTML files and web pages.

%description -l pl.UTF-8
GNOME Web Photographer to narzędzie do generowania pełnowymiarowych
plików obrazów i miniaturek.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install thumbnailer.schemas

%preun
%gconf_schema_uninstall thumbnailer.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING MAINTAINERS NEWS README TODO
%{_sysconfdir}/gconf/schemas/thumbnailer.schemas
%attr(755,root,root) %{_bindir}/gnome-web-photo
%dir %{_datadir}/gnome-web-photo
%{_datadir}/gnome-web-photo/prefs.js
%{_datadir}/gnome-web-photo/style.css
