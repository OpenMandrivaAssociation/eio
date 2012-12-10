#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/eio eio; \
#cd eio; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf eio-$PKG_VERSION.tar.xz eio/ --exclude .svn --exclude .*ignore

#% define svndate 20120103
#% define svnrev 	66800

%define major	1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	E17 Input Output Library
Name:		eio
Version:	1.7.3
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz

BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(eet) >= 1.7.0
BuildRequires:	pkgconfig(ecore) >= 1.7.0
BuildRequires:	pkgconfig(eina) >= 1.7.0

%description
This library is intended to provide non blocking IO by using thread for all
operation that may block. It depends only on eina and ecore right now. It
should integrate all the features/functions of Ecore_File that could block.

This should become one day part of what we call the EFL and be a dependence
of E17. Feel free to contribute, help is always appreciated !

%package -n %{libname}
Summary:	Eio library
Group:		System/Libraries

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Summary:	Eio headers, libraries, documentation and test programs
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Headers and libraries from %{name}

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS README ChangeLog NEWS
%{_includedir}/%{name}*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc



%changelog
* Wed Jun 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.1-1
+ Revision: 807155
- version update 1.0.1

* Wed Jan 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.1.0.66800-0.20120103.1
+ Revision: 756098
- new snapshot 66800
- sync spec with UnityLinux
- cleaned up spec

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 0.1.0.55225-1mdv2011.0
+ Revision: 622801
- new version 0.1.0.55225

* Tue Nov 16 2010 Funda Wang <fwang@mandriva.org> 0.1.0.54504-1mdv2011.0
+ Revision: 597992
- import eio

