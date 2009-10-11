%define name    krecipes
%define version 2.0
%define svn alpha3
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
Krecipes is a new Open Source project for an exciting world 
that is almost forgotten in the Tux world: COOKING (yummy! ;-)

The goal of this projects was to create a KDE Recipe Tool that:

    * Can manage a recipe database with an easy to use interface
    * Allows creation/removal of new ingredients and units
    * Helps with diets, calculating amount of calories, 
		vitamines, carbohydrates... per recipe
    * Creates shopping lists, and daily suggestions for a given diet type
    * Should be as flexible as possible to have the possibility to 
		extend it in future.

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
