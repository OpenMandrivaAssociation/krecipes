%define name    krecipes
%define version 1.1
%define svn 802572
%define release %mkrel 0.%svn.1



Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   Krecipes - Your Way to Cook with Tux 
License:   GPL
URL:       http://krecipes.sourceforge.net/
Group:     Toys
Source:    http://ovh.dl.sourceforge.net/sourceforge/krecipes/%name-%version.%svn.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: sqlite-devel

%description
Krecipes is a new Open Source project for an exciting world 
that is almost forgotten in the Tux world: COOKING (yummy! ;-)

The goal of this projects was to create a KDE Recipe Tool that:

    * Can manage a recipe database with an easy to use interface
    * Allows creation/removal of new ingredients and units
    * Helps with diets, calculating amount of calories, 
		vitamines, carbohydrates... per recipe
    * Creates shopping lists, and daily suggestions for a given diet type
    * Is based on MySQL (1) so it could be possible to generate a KSN(2)
    * Should be as flexible as possible to have the possibility to 
		extend it in future.

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files 
#-f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/krecipes
%{_kde_datadir}/applications/kde4/krecipes.desktop
%{_kde_appsdir}/krecipes  
%{_kde_iconsdir}/hicolor/*/apps/krecipes.png
%doc %{_kde_docdir}/HTML/en/krecipes

#--------------------------------------------------------------------

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}

%build
export PATH=$PATH:$QTDIR/bin 

%cmake_kde4

%install
rm -rf %buildroot
cd build
%{makeinstall_std}

#(nl) Workaround for missing translations
# FIXME
#for lang in bg ca cy de en_GB et fr is lt nb pl pt_BR ru sl sr@Latn ta az br cs da el es fi ga it mt nl pt ro rw sr sv tr;
#do
#   cd po/$lang && make && /usr/bin/install -c -p -m 644 krecipes.gmo %buildroot/usr/share/locale/$lang/LC_MESSAGES/krecipes.mo && cd ../..
#done
        


install -d %buildroot/%{_menudir}

#%find_lang %{name}

%clean
rm -rf %{buildroot}

