
%define		theme	livecd

Summary:	Bootsplash - PLD LiveCD with KDE4 by shadzik theme
Summary(de.UTF-8):	Bootsplash - PLD LiveCD mit KDE4 by shadzik Thema für Bootsplash
Summary(pl.UTF-8):	Bootsplash - motyw PLD LiveCD z KDE4 wg shadzika
Name:		bootsplash-theme-%{theme}
Version:	1.1
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://livecd.pld-linux.pl/%{name}-%{version}.tar.bz2
# Source0-md5:	310b9d647cf83a57c28b1ccd1456d2cc
URL:		http://livecd.pld-linux.pl/
Requires:	bootsplash
Provides:	bootsplash-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD LiveCD with KDE4 theme by shadzik for bootsplash.

%description -l de.UTF-8
PLD LiveCD mit KDE4 by shadzik Thema für Bootsplash.

%description -l pl.UTF-8
Motyw PLD LiveCD z KDE4 do bootsplash wg shadzika.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
THEME_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/bootsplash/themes/%{theme}
install -d $THEME_DIR/{config,images}
install %{theme}/config/*.cfg $THEME_DIR/config
install %{theme}/images/*.jpg $THEME_DIR/images

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/bootsplash/themes/%{theme}
