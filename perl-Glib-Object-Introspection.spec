#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pnam	Glib-Object-Introspection
Summary:	Perl Glib Object-Introspection bindings
Summary(pl.UTF-8):	Wiązania Glib Object-Introspection dla Perla
Name:		perl-Glib-Object-Introspection
Version:	0.049
Release:	3
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	0d8ab0bf9c4d0a72eb35c16a2ff10d42
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gobject-introspection-devel >= 1.60.0
BuildRequires:	libffi-devel >= 3.0.0
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.00
BuildRequires:	perl-Glib-devel >= 1.320
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig(libffi) >= 3.0.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel >= 2.0
%endif
Requires:	gobject-introspection >= 1.60.0
Requires:	perl-Glib >= 1.320
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glib::Object::Introspection uses the gobject-introspection and libffi
projects to dynamically create Perl bindings for a wide variety of
libraries. Examples include gtk+, webkit, libsoup and many more.

%description -l pl.UTF-8
Glib::GObject::Introspection wykorzystuje projekty
gobject-introspection oraz libffi do dynamicznego tworzenia wiązań
Perla do wielu bibliotek, na przykład gtk+, webkit, libsoup.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Glib/Object/Introspection/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/perli11ndoc
%dir %{perl_vendorarch}/Glib/Object
%{perl_vendorarch}/Glib/Object/Introspection.pm
%dir %{perl_vendorarch}/Glib/Object/Introspection
%{perl_vendorarch}/Glib/Object/Introspection/Install
%dir %{perl_vendorarch}/auto/Glib/Object
%dir %{perl_vendorarch}/auto/Glib/Object/Introspection
%attr(755,root,root) %{perl_vendorarch}/auto/Glib/Object/Introspection/Introspection.so
%{_mandir}/man3/Glib::Object::Introspection.3pm*
