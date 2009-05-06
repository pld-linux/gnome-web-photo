Summary:	Tool to generate full-size image files and thumbnails
Summary(pl.UTF-8):	Narzędzie do generowania pełnowymiarowych plików obrazów i miniaturek
Name:		gnome-web-photo
Version:	0.7
Release:	2
License:	GPL
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-web-photo/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	90c556a29ba57b8d1629f21705beba54
Patch0:		%{name}-libxul.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	xulrunner-devel >= 1.9-5
Requires(post,preun):	GConf2
%requires_eq_to	xulrunner xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# we have strict deps for it
%define		_noautoreq	libxpcom.so

%description
GNOME Web Photographer is a tool to generate full-size image files and
thumbnails from HTML files and web pages.

%description -l pl.UTF-8
GNOME Web Photographer to narzędzie do generowania pełnowymiarowych
plików obrazów i miniaturek.

%prep
%setup -q
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/gnome-web-print
%attr(755,root,root) %{_bindir}/gnome-web-thumbnail
%dir %{_datadir}/gnome-web-photo
%{_datadir}/gnome-web-photo/prefs.js
%{_datadir}/gnome-web-photo/style.css
