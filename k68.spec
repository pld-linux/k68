Summary:	Communication software for t68i phone
Summary(pl):	Oprogramowanie komunikacyjne dla telefon t68i
Name:		k68
Version:	0.2
Release:	0.1
License:	GPL
Group:		Applications/Communications
Vendor:		-
Source0:	http://dl.sourceforge.net/sourceforge/k68/%{name}-%{version}.tar.bz2
#Source0-MD5:	3f31ef8fd7bcd2758dacd995c95f717a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
empty

%prep
%setup -q

%build
rm -f missing
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/*
%{_datadir}/mimelnk/*/*
