Summary:	Communication software for t68i phone
Summary(pl):	Oprogramowanie komunikacyjne dla telefonu t68i
Name:		k68
Version:	0.2.1
Release:	5
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/k68/%{name}-%{version}.tar.bz2
# Source0-md5:	82d1306995bc8b10922108e17127a708
Source1:	http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:	81e0b2f79ef76218381270960ac0f55f
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-openobex-pkgconfig.patch
Patch2:		kde-ac260.patch
URL:		http://k68.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	openobex-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K68 is a tool for communicating with a Sony Ericsson(R) T68i or T68
mobile phone.

%description -l pl
K68 to narzêdzie do komunikacji z telefonami komórkowymi Sony
Ericsson(R) T68i oraz T68.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# be permissive - BDADDR_ANY from <bluetooth/bluetooth.h> used in k68.cpp
# is a compound statement, which ISO C++ forbids
CXXFLAGS="%{rpmcflags} -fpermissive"
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

mv   $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities,%{_desktopdir}}/k68.desktop
echo "Categories=Qt;KDE;Office;PDA;" >> $RPM_BUILD_ROOT%{_desktopdir}/k68.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/k68.desktop
%{_datadir}/mimelnk/*/*
