%define svn beta1

Summary:	Your Way to Cook with Tux
Name:		krecipes
Version:	2.0
Release:	0.%{svn}.3
License:	GPLv2+
Group:		Toys
Url:		http://krecipes.sourceforge.net/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/krecipes/%{name}-%{version}-%{svn}.tar.gz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	pkgconfig(sqlite)
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel

%description
A highly configurable recipe manager, designed to make organizing your
personal recipes collection fast and easy. Features include: shopping
lists, nutrient analysis, advanced search, recipe ratings, import/export
various formats, and more.

%files -f %{name}.lang
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}
%{_kde_iconsdir}/*/*/*/*
%{_datadir}/mime/packages/%{name}-mime.xml

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-%{svn}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

