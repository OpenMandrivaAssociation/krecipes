%define name    krecipes
%define version 2.0
%define svn alpha5
%define release %mkrel 0.%svn.1

Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   Krecipes - Your Way to Cook with Tux 
License:   GPLv2+
URL:       http://krecipes.sourceforge.net/
Group:     Toys
Source:    http://ovh.dl.sourceforge.net/sourceforge/krecipes/%name-%version-%svn.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: sqlite3-devel
BuildRequires: qimageblitz-devel
BuildRequires: libxml2-devel
BuildRequires: mysql-devel
BuildRequires: postgresql-devel

%description
A highly configurable recipe manager, designed to make organizing your
personal recipes collection fast and easy. Features include: shopping
lists, nutrient analysis, advanced search, recipe ratings, import/export
various formats, and more.

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/krecipes
%{_kde_datadir}/applications/kde4/krecipes.desktop
%{_kde_appsdir}/krecipes  
%{_kde_iconsdir}/*/*/*/*
%{_datadir}/mime/packages/krecipes-mime.xml

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version-%svn

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
