Summary:	Tool to generate full-size image files and thumbnails
Summary(pl.UTF-8):	Narzędzie do generowania pełnowymiarowych plików obrazów i miniaturek
Name:		gnome-web-photo
Version:	0.10.6
Release:	1
License:	GPL
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-web-photo/0.10/%{name}-%{version}.tar.xz
# Source0-md5:	6fbf72173149ffae57e66605e4898113
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-webkit3-devel >= 1.1.23
BuildRequires:	intltool >= 0.40.6
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-web-photo
%attr(755,root,root) %{_bindir}/gnome-web-print
%attr(755,root,root) %{_bindir}/gnome-web-thumbnail
%dir %{_datadir}/gnome-web-photo
%{_datadir}/gnome-web-photo/style.css
%{_datadir}/thumbnailers/gnome-web-photo.thumbnailer
