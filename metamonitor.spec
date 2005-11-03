Summary:	MetaMonitor - log monitoring tool for KDE
Summary(pl):	MetaMonitor - narzêdzie do monitorowanie logów dla KDE
Name:		metamonitor
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/metamonitor/%{name}-%{version}.tar.bz2
# Source0-md5:	912b515b98a917af57ecd0bb46afa2a1
URL:		http://metamonitor.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MetaMonitor is a simple program written for KDE, which watches the
syslog's or metalog's log file and pops up the window whenever the new
message comes. You can specify the file to watch and a regular
expression for parsing the log line, so you can watch other than log
files too.

%description -l pl
MetaMonitor jest prostym programem monitoruj±cym loggery systemowe
(syslog, metalog) i wyswietlaj±cym nadchodz±ce komunikaty w dymkach.
Mo¿esz tak¿e wybraæ dowolny inny plik z logami i filtrowaæ
interesuj±ce ciê wiadomo¶ci za pomoc± wyra¿eñ regularnych.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__aclocal}
%{__autoconf}

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_iconsdir}/*/*/apps/%{name}.png
