Summary:	Communication software for t68i phone
Summary(pl):	Oprogramowanie komunikacyjne dla telefonu t68i
Name:		k68
Version:	0.2
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/k68/%{name}-%{version}.tar.bz2
#Source0-MD5:	3f31ef8fd7bcd2758dacd995c95f717a
URL:		http://k68.sourceforge.net/
BuildRequires:	bluez-libs-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	openobex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
K68 is a tool for communicating with a Sony Ericsson(R) T68i or T68
mobile phone.

%description -l pl
K68 to narzêdzie do komunikacji z telefonami komórkowymi Sony
Ericsson(R) T68i oraz T68.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
# be permissive - BDADDR_ANY from <bluetooth/bluetooth.h> used in k68.cpp
# is a compound statement, which ISO C++ forbids
CXXFLAGS="%{rpmcflags} -fpermissive"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/*.desktop
%{_datadir}/mimelnk/*/*
