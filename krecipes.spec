%define name    krecipes
%define version 2.0
%define svn beta1
%define release %mkrel 0.%svn.1

Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   - Your Way to Cook with Tux 
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


%changelog
* Fri Jul 09 2010 Funda Wang <fwang@mandriva.org> 2.0-0.beta1.1mdv2011.0
+ Revision: 549884
- 2.0 beta1

* Wed Jan 27 2010 Funda Wang <fwang@mandriva.org> 2.0-0.alpha6.1mdv2010.1
+ Revision: 497156
- new version 2.0 alpha6

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 2.0-0.alpha5.1mdv2010.1
+ Revision: 492420
- new version 2.0 alpha 5

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 2.0-0.alpha4.1mdv2010.1
+ Revision: 463292
- 2.0 alpha4

* Sun Oct 11 2009 Funda Wang <fwang@mandriva.org> 2.0-0.alpha3.1mdv2010.0
+ Revision: 456597
- update description
- New version 2.0 alpha3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - New snapshot ( asked by upstream dev)

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.1-0.802572.1mdv2009.0
+ Revision: 218422
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - Move to kde4 version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Aug 21 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-21 10:16:32 (56935)
- krecipes-0.9.1-3mdv2007.0
- Fix translations (ticket 19846)

* Fri Jul 28 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-07-28 08:58:20 (42358)
- Fix menu entry

* Fri Jul 28 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-07-28 08:56:48 (42357)
- Fix menu entry

* Tue Jul 25 2006 Laurent Montel <lmontel@mandriva.com>
+ 2006-07-25 07:26:02 (42054)
Don't requires meta package kdebase

* Thu Jun 15 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-06-15 17:57:36 (37322)
- Increase release
- Rebuild to generate category
- Add Warning

* Thu Jun 15 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-06-15 17:30:29 (37320)
import krecipes-0.9.1-1mdk

* Sun Dec 04 2005 Laurent MONTEL <lmontel@mandriva.com> 0.9.1-1
- 0.9.1

* Wed Nov 30 2005 Laurent MONTEL <lmontel@mandriva.com> 0.9-1
- 0.9.0

* Sun Nov 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.1-2mdk
- Fix ticket #19846

* Tue Aug 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.1-1mdk
- First mandriva release

