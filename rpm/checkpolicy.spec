# based on work by The Fedora Project (2017)
# Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

%define libselinuxver 2.7-1
%define libsepolver 2.7-1

Summary: SELinux policy compiler
Name: checkpolicy
Version: 2.7
Release: 4%{?dist}
License: GPLv2
Source: %{name}-%{version}.tar.bz2
#Conflicts: selinux-policy-base < 3.13.1-138
BuildRequires: gcc
BuildRequires: byacc bison flex libsepol-static >= %{libsepolver} libselinux-devel  >= %{libselinuxver} 

%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

This package contains checkpolicy, the SELinux policy compiler.  
Only required for building policies. 

%prep
%setup -q -n %{name}-%{version}/upstream

%build
make clean
# only build checkpolicy
cd %{name}
make LIBDIR="%{_libdir}" CFLAGS="%{optflags}" 
cd test
make LIBDIR="%{_libdir}" CFLAGS="%{optflags}" 

%install
# only install checkpolicy
cd %{name}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
make LIBDIR="%{_libdir}" DESTDIR="${RPM_BUILD_ROOT}" install
install test/dismod ${RPM_BUILD_ROOT}%{_bindir}/sedismod
install test/dispol ${RPM_BUILD_ROOT}%{_bindir}/sedispol

%files
%doc %{name}/COPYING
%{_bindir}/checkpolicy
%{_bindir}/checkmodule
%{_mandir}/man8/checkpolicy.8.gz
%{_mandir}/man8/checkmodule.8.gz
%{_bindir}/sedismod
%{_bindir}/sedispol
