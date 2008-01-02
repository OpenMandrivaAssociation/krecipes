# THIS PACKAGE IS HOSTED AT MANDRIVA SVN
# PLEASE DO NOT UPLOAD DIRECTLY BEFORE COMMIT

%define name    krecipes
%define version 0.9.1
%define release %mkrel 4
%define __libtoolize /bin/true
%define __cputoolize /bin/true



Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   Krecipes - Your Way to Cook with Tux 
License:   GPL
URL:       http://krecipes.sourceforge.net/
Group:     Toys
Source:    http://ovh.dl.sourceforge.net/sourceforge/krecipes/%name-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: kdelibs-devel >= 3.2
BuildRequires: sqlite-devel
Requires: kdelibs-common
Requires: kdebase-progs

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

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%attr(0755,root,root) %{_bindir}/%{name}

%{_menudir}/%{name}

%{_datadir}/applnk/Utilities/%{name}.desktop
%{_datadir}/apps/%{name}/data/*.txt
%{_datadir}/apps/%{name}/data/*.sql
%{_datadir}/apps/%{name}/data/*.kreml
%{_datadir}/apps/%{name}/%{name}ui.rc
%{_datadir}/apps/%{name}/layouts/*.klo

%_datadir/apps/krecipes/icons/crystalsvg/128x128/mimetypes/krecipes_file.png
%_datadir/apps/krecipes/icons/crystalsvg/16x16/mimetypes/krecipes_file.png
%_datadir/apps/krecipes/icons/crystalsvg/32x32/mimetypes/krecipes_file.png
%_datadir/apps/krecipes/icons/crystalsvg/64x64/mimetypes/krecipes_file.png

%_datadir/icons/crystalsvg/128x128/mimetypes/krecipes_file.png
%_datadir/icons/crystalsvg/16x16/mimetypes/krecipes_file.png
%_datadir/icons/crystalsvg/32x32/mimetypes/krecipes_file.png
%_datadir/icons/crystalsvg/64x64/mimetypes/krecipes_file.png
%_datadir/mimelnk/application/x-krecipes-backup.desktop
%_datadir/mimelnk/application/x-krecipes-recipes.desktop


%dir %_docdir/HTML/da/%{name}/
%doc %_docdir/HTML/da/%{name}/common
%doc %_docdir/HTML/da/%{name}/*.bz2
%doc %_docdir/HTML/da/%{name}/*.docbook

%dir %_docdir/HTML/en/%{name}/
%doc %_docdir/HTML/en/%{name}/*.png
%doc %_docdir/HTML/en/%{name}/common
%doc %_docdir/HTML/en/%{name}/*.docbook
%doc %_docdir/HTML/en/%{name}/*.bz2

%dir %_docdir/HTML/es/%{name}/
%doc %_docdir/HTML/es/%{name}/*.png


%dir %_docdir/HTML/et/%{name}/
%doc %_docdir/HTML/et/%{name}/common
%doc %_docdir/HTML/et/%{name}/*.bz2
%doc %_docdir/HTML/et/%{name}/*.docbook

%dir %_docdir/HTML/pt/%{name}/
%doc %_docdir/HTML/pt/%{name}/common
%doc %_docdir/HTML/pt/%{name}/*.bz2
%doc %_docdir/HTML/pt/%{name}/*.docbook

%dir %_docdir/HTML/sv/%{name}/
%doc %_docdir/HTML/sv/%{name}/*.png
%doc %_docdir/HTML/sv/%{name}/common
%doc %_docdir/HTML/sv/%{name}/*.docbook
%doc %_docdir/HTML/sv/%{name}/*.bz2

%{_iconsdir}/hicolor/128x128/apps/krecipes.png
%{_iconsdir}/hicolor/16x16/apps/krecipes.png
%{_iconsdir}/hicolor/22x22/apps/krecipes.png
%{_iconsdir}/hicolor/32x32/apps/krecipes.png
%{_iconsdir}/hicolor/48x48/apps/krecipes.png
%{_iconsdir}/hicolor/64x64/apps/krecipes.png

%{_datadir}/apps/%{name}/pics/*.png
%{_datadir}/apps/%{name}/icons/crystalsvg/16x16/actions/*.png
%{_datadir}/apps/%{name}/icons/crystalsvg/22x22/actions/*.png
%{_datadir}/apps/%{name}/icons/crystalsvg/32x32/actions/*.png
%{_datadir}/apps/%{name}/icons/crystalsvg/48x48/actions/*.png


#--------------------------------------------------------------------

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{version}

%build
export PATH=$PATH:$QTDIR/bin 

%configure --disable-rpath \
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" 
%endif

%install
rm -rf %buildroot
%{makeinstall_std}

#(nl) Workaround for missing translations
# FIXME
for lang in bg ca cy de en_GB et fr is lt nb pl pt_BR ru sl sr@Latn ta az br cs da el es fi ga it mt nl pt ro rw sr sv tr;
do
   cd po/$lang && make && /usr/bin/install -c -p -m 644 krecipes.gmo %buildroot/usr/share/locale/$lang/LC_MESSAGES/krecipes.mo && cd ../..
done
        


install -d %buildroot/%{_menudir}

kdedesktop2mdkmenu.pl %{name} "More Applications/Databases" $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/%{name}.desktop  $RPM_BUILD_ROOT%{_menudir}/%{name} x11 Krecipes

%find_lang %{name}

%clean
rm -rf %{buildroot}

