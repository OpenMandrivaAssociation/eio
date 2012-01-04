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

%define svndate 20120103
%define svnrev 	66800

%define	major	0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary: 	E17 Input Output Library
Name: 		eio
Version:	0.1.0.%{svnrev}
Release:	0.%{svndate}.1
License: 	LGPLv2+
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source0:	%{name}-%{version}.tar.xz

Buildrequires: gettext-devel
BuildRequires: pkgconfig(ecore) >= 1.0.0
BuildRequires: pkgconfig(eina) >= 1.0.0

%description
This library is intended to provide non blocking IO by using thread for all
operation that may block. It depends only on eina and ecore right now. It
should integrate all the features/functions of Ecore_File that could block.

This should become one day part of what we call the EFL and be a dependence
of E17. Feel free to contribute, help is always appreciated !

%package -n %{libname}
Summary:    Eio library
Group:      System/Libraries

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Summary:    Eio headers, libraries, documentation and test programs
Group:      Development/Other
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
Headers and libraries from %{name}

%prep
%setup -qn %{name}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS README ChangeLog NEWS
%{_includedir}/%{name}*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc

