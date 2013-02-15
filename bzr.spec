# TODO
# split the tools from main package ?
# split the doc ?
Name:           bzr
Epoch:          0
Version:        2.5.1
Release:        3
Summary:        Next-generation distributed version control
Group:          Development/Other
License:        GPLv2+
URL:            http://www.bazaar-vcs.org/
Source0:        https://launchpad.net/bzr/%{version}/%{version}/+download/bzr-%{version}.tar.gz
Source1:	https://launchpad.net/bzr/%{version}/%{version}/+download/bzr-%{version}.tar.gz.sig
BuildRoot:      %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:  python-devel python-paramiko zlib-devel

%description
Bazaar is a distributed revision control system. It allows team members to
branch and merge upstream code very easily.

Distributed revision control systems allow multiple people to have their
own branch of a project, and merge code efficiently between them. This
enables new contributors to immediately have access to the full tools that
previously have been limited to just the committers to a project.

%prep
%setup -q -n %{name}-%{version}

%check
# run test in /tmp to avoid lock problems with nfs on build cluster
# sadely, it's not enough: bzr tests are trying to rebuild bzr, and
# so must be run in the bzr build dir
# cd /tmp
# $OLDPWD/bzr selftest

# (misc) broken by diff binary test, will investigate later
# still broken with 0.11
# still broken with 0.12
# still broken with 0.13, maybe du to a local server listening , as pycurl test fail
# still broken with 0.15
export TMPDIR=/tmp
#./bzr selftest

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}/%_prefix
mkdir -p %{buildroot}/%_mandir/
mv %{buildroot}/%_prefix/man/* %{buildroot}/%_mandir/
# remove as they are packaged externally
rm -Rf %{buildroot}/%py_platsitedir/bzrlib/util/elementtree

find %{buildroot}/%py_platsitedir -name '*.pyc' | xargs rm -f

# install bash completion
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d/
cp contrib/bash/bzr %{buildroot}/%{_sysconfdir}/bash_completion.d/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc  doc contrib NEWS README TODO
%_bindir/bzr
%py_platsitedir/bzrlib/
%py_platsitedir/*egg-info
%_mandir/man1/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/bzr


%changelog
* Wed May 23 2012 Crispin Boylan <crisb@mandriva.org> 0:2.5.1-2
+ Revision: 800312
- Dont package tools

* Wed May 23 2012 Crispin Boylan <crisb@mandriva.org> 0:2.5.1-1
+ Revision: 800260
- New release

* Tue Feb 28 2012 Crispin Boylan <crisb@mandriva.org> 0:2.5.0-1
+ Revision: 781243
- New release

* Mon Nov 14 2011 Crispin Boylan <crisb@mandriva.org> 0:2.4.2-1
+ Revision: 730545
- New release

* Mon Sep 12 2011 Crispin Boylan <crisb@mandriva.org> 0:2.4.1-1
+ Revision: 699446
- New release

* Sat Aug 13 2011 Crispin Boylan <crisb@mandriva.org> 0:2.4.0-1
+ Revision: 694339
- New release

* Sun Aug 07 2011 Crispin Boylan <crisb@mandriva.org> 0:2.3.4-1
+ Revision: 693587
- New release

* Fri Mar 18 2011 Crispin Boylan <crisb@mandriva.org> 0:2.3.1-1
+ Revision: 646337
- Add bins
- New release

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0:2.3.0-2
+ Revision: 640425
- rebuild to obsolete old packages

* Mon Feb 14 2011 Crispin Boylan <crisb@mandriva.org> 0:2.3.0-1
+ Revision: 637677
- Drop patch 0 (merged upstream)
- New release

* Sat Jan 29 2011 Crispin Boylan <crisb@mandriva.org> 0:2.2.3-1
+ Revision: 633847
- New release

* Thu Dec 23 2010 Crispin Boylan <crisb@mandriva.org> 0:2.2.2-1mdv2011.0
+ Revision: 623984
- New release

* Sat Nov 13 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0:2.2.1-3mdv2011.0
+ Revision: 597031
- added fix for lp#612096 when using xmlrpclib with python-2.7

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0:2.2.1-2mdv2011.0
+ Revision: 590147
- rebuild for python 2.7

* Tue Oct 05 2010 Crispin Boylan <crisb@mandriva.org> 0:2.2.1-1mdv2011.0
+ Revision: 583072
- Fix destdir longer than base dir
- New release

* Sat Aug 07 2010 Crispin Boylan <crisb@mandriva.org> 0:2.2.0-1mdv2011.0
+ Revision: 567294
- New release

* Sun Jun 27 2010 Crispin Boylan <crisb@mandriva.org> 0:2.1.2-1mdv2011.0
+ Revision: 549204
- New release

* Thu Mar 25 2010 Crispin Boylan <crisb@mandriva.org> 0:2.1.1-1mdv2010.1
+ Revision: 527363
- New release

* Wed Feb 17 2010 Crispin Boylan <crisb@mandriva.org> 0:2.1.0-1mdv2010.1
+ Revision: 506924
- New release

* Wed Dec 30 2009 Crispin Boylan <crisb@mandriva.org> 0:2.0.3-1mdv2010.1
+ Revision: 483832
- New release

* Sun Nov 08 2009 Crispin Boylan <crisb@mandriva.org> 0:2.0.2-1mdv2010.1
+ Revision: 462857
- New release

* Sat Oct 17 2009 Crispin Boylan <crisb@mandriva.org> 0:2.0.1-1mdv2010.0
+ Revision: 457993
- New release

* Wed Sep 23 2009 Crispin Boylan <crisb@mandriva.org> 0:2.0.0-1mdv2010.0
+ Revision: 447680
- 2.0.0 final

* Tue Sep 15 2009 Crispin Boylan <crisb@mandriva.org> 0:2.0-0.1mdv2010.0
+ Revision: 442935
- 2.0 rc2
- New release

* Sun Aug 30 2009 Crispin Boylan <crisb@mandriva.org> 0:1.18-1mdv2010.0
+ Revision: 422369
- New release

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - removed buildreq for python-pyrex, as it is only needed for development

* Tue Jul 21 2009 Frederik Himpe <fhimpe@mandriva.org> 0:1.17-1mdv2010.0
+ Revision: 398351
- Update to new version 1.17

* Thu Jun 18 2009 Frederik Himpe <fhimpe@mandriva.org> 0:1.16-1mdv2010.0
+ Revision: 387138
- update to new version 1.16

* Wed Jun 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0:1.15.1-1mdv2010.0
+ Revision: 384891
- Update to new version 1.15.1

* Sat May 23 2009 Frederik Himpe <fhimpe@mandriva.org> 0:1.15-1mdv2010.0
+ Revision: 379050
- Update to new version 1.15

* Sun May 03 2009 Crispin Boylan <crisb@mandriva.org> 0:1.14.1-1mdv2010.0
+ Revision: 370992
- new release

* Fri May 01 2009 Crispin Boylan <crisb@mandriva.org> 0:1.14-1mdv2010.0
+ Revision: 369521
- BuildRequires zlib
- New release
- New release

* Mon Mar 16 2009 Crispin Boylan <crisb@mandriva.org> 0:1.13-1mdv2009.1
+ Revision: 355625
- New release

* Sat Feb 14 2009 Crispin Boylan <crisb@mandriva.org> 0:1.12-1mdv2009.1
+ Revision: 340238
- New binaries
- New release

* Tue Jan 20 2009 Crispin Boylan <crisb@mandriva.org> 0:1.11-1mdv2009.1
+ Revision: 331539
- New version

* Wed Dec 24 2008 Michael Scherer <misc@mandriva.org> 0:1.10-4mdv2009.1
+ Revision: 318359
- rebuild for new python

* Tue Dec 09 2008 Funda Wang <fwang@mandriva.org> 0:1.10-3mdv2009.1
+ Revision: 312213
- do not obsolete bazaar

* Tue Dec 09 2008 Funda Wang <fwang@mandriva.org> 0:1.10-2mdv2009.1
+ Revision: 312081
- obsoletes bazaar

* Sat Dec 06 2008 Crispin Boylan <crisb@mandriva.org> 0:1.10-1mdv2009.1
+ Revision: 310927
- New version

* Fri Nov 07 2008 Crispin Boylan <crisb@mandriva.org> 0:1.9-1mdv2009.1
+ Revision: 300438
- Remove old sources
- New tarballs
- New version, remove obsolete requires

* Sat Oct 11 2008 Frederik Himpe <fhimpe@mandriva.org> 0:1.7.1-1mdv2009.1
+ Revision: 291670
- Update to new version 1.7.1

* Sat Sep 06 2008 Frederik Himpe <fhimpe@mandriva.org> 0:1.6.1-1mdv2009.0
+ Revision: 281809
- Update to new version 1.6.1
- Adapt to license pocliy
- Don't package COPYING.txt and INSTALL

* Tue Aug 26 2008 Jérôme Soyer <saispo@mandriva.org> 0:1.6-1mdv2009.0
+ Revision: 276171
- New release

* Fri Jun 13 2008 Michael Scherer <misc@mandriva.org> 0:1.5-1mdv2009.0
+ Revision: 218995
- upgrade to 1.5

* Wed May 14 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 0:1.4-1mdv2009.0
+ Revision: 207320
- new version 1.4
- new source URLs

* Mon Mar 03 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 0:1.2-1mdv2008.1
+ Revision: 177971
- new version 1.2

* Thu Jan 17 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 0:1.1-2mdv2008.1
+ Revision: 154189
- added a friendlier description
- new version 1.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 14 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0:1.0-1mdv2008.1
+ Revision: 119907
- new version 1.0

* Wed Nov 14 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.92-1mdv2008.1
+ Revision: 108732
- new version 0.92

* Fri Oct 12 2007 Jérôme Soyer <saispo@mandriva.org> 0.91-1mdv2008.1
+ Revision: 97325
- New release 0.91

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - added NEWS, INSTALL and COPYING.txt to docs

* Wed Aug 29 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.90-1mdv2008.0
+ Revision: 74860
- with the new pyrex modules, remove noarch
- new version 0.90
- now requires python-pyrex

* Mon Jul 30 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.18-2mdv2008.0
+ Revision: 56618
- removed requires for python-pyrex, only 0.19 will need it

* Tue Jul 17 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.18-1mdv2008.0
+ Revision: 52867
- new version 0.18

* Mon Jun 18 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.17-1mdv2008.0
+ Revision: 40819
- new version 0.17

* Mon May 07 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.16-1mdv2008.0
+ Revision: 24860
- upgrade to 0.16

* Sun Apr 22 2007 Michael Scherer <misc@mandriva.org> 0.15-1mdv2008.0
+ Revision: 16978
- upgrade to 0.15

