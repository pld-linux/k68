Summary:	Communication software for t68i phone
Summary(pl):	Oprogramowanie komunikacyjne dla telefonu t68i
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
Oprogramowanie komunikacyjne dla telefonu t68i.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/*
%{_datadir}/mimelnk/*/*
