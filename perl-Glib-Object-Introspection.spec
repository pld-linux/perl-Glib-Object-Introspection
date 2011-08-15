#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pnam	Glib-Object-Introspection
%include	/usr/lib/rpm/macros.perl
Summary:	Perl Glib Object-Introspection bindings
Summary(pl.UTF-8):	Wiązania Glib Object-Introspection dla Perla
Name:		perl-Glib-Object-Introspection
Version:	0.001
# place real perl-Glib version and set to 1 when required perl-Glib is released
Release:	0.1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	c602cef2453692334ac5c34564c16662
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.00
BuildRequires:	perl-Glib-devel > 1.224
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel >= 2.0
%endif
Requires:	gobject-introspection >= 0.10.0
Requires:	perl-Glib > 1.224
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
%dir %{perl_vendorarch}/Glib/Object
%{perl_vendorarch}/Glib/Object/Introspection.pm
%dir %{perl_vendorarch}/Glib/Object
%dir %{perl_vendorarch}/Glib/Object/Introspection
%{perl_vendorarch}/Glib/Object/Introspection/Install
%dir %{perl_vendorarch}/auto/Glib/Object
%dir %{perl_vendorarch}/auto/Glib/Object/Introspection
%attr(755,root,root) %{perl_vendorarch}/auto/Glib/Object/Introspection/Introspection.so
%{perl_vendorarch}/auto/Glib/Object/Introspection/Introspection.bs
%{_mandir}/man3/Glib::Object::Introspection.3pm*