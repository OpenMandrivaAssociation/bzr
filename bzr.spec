# TODO
# split the tools from main package ?
# split the doc ?
Name:           bzr
Epoch:          0
Version:        2.5.0
Release:        %mkrel 1
Summary:        Next-generation distributed version control
Group:          Development/Other
License:        GPLv2+
URL:            http://www.bazaar-vcs.org/
Source0:        https://launchpad.net/bzr/%{version}/%{version}/+download/bzr-%{version}.tar.gz
Source1:	https://launchpad.net/bzr/%{version}/%{version}/+download/bzr-%{version}.tar.gz.sig
BuildRoot:      %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:  python-devel python-paramiko zlib-devel
%define _provides_exceptions perl(

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
%doc  doc contrib NEWS README TODO tools
%_bindir/bzr
%py_platsitedir/bzrlib/
%py_platsitedir/*egg-info
%_mandir/man1/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/bzr
