# TODO
# split the tools from main package ?
# split the doc ?

Name:           bzr
Version:        0.90
Release:        %mkrel 1
Summary:        Next-generation distributed version control 
Group:          Development/Other
License:        GPL
URL:            http://www.bazaar-vcs.org/
Source0:        http://bazaar-vcs.org/releases/src/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}.tar.gz.sig
BuildRoot:      %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:  python-devel python-paramiko python-pyrex
Requires:       python-urlgrabber python-celementtree
%define _provides_exceptions perl(
# force buildir to be able to run test on build cluster
%define _builddir /tmp

%description
Bazaar-NG (or bzr) is a project of Canonical to develop an open source
distributed version control system that is powerful, friendly, and scalable. 
Version control means a system that keeps track of previous revisions of 
software source code or similar information and helps people work on it 
in teams.

%prep
%setup -q

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
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=$RPM_BUILD_ROOT/%_prefix
mkdir -p $RPM_BUILD_ROOT/%_mandir/
mv $RPM_BUILD_ROOT/%_prefix/man/* $RPM_BUILD_ROOT/%_mandir/
# remove as they are packaged externally
rm -Rf $RPM_BUILD_ROOT/%py_puresitedir/bzrlib/util/urlgrabber
rm -Rf $RPM_BUILD_ROOT/%py_puresitedir/bzrlib/util/elementtree

find $RPM_BUILD_ROOT/%py_puresitedir -name '*.pyc' | xargs rm -f 

# install bash completion
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/
cp contrib/bash/bzr $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc  doc contrib README TODO tools
%_bindir/bzr
%py_puresitedir/bzrlib/
%py_platsitedir/bzrlib/*.so
%py_puresitedir/*egg-info
%_mandir/man1/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/bzr


