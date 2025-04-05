Name: bionic_translation
Version: 1742824834.5563440
Release: 0
URL: https://gitlab.com/android_translation_layer/bionic_translation
License:        GPL-3.0-or-later
Summary: a set of libraries for loading bionic-linked .so files on musl/glibc
BuildRequires: rpm_macro(meson)
BuildRequires: rpm_macro(meson_build)
BuildRequires: rpm_macro(meson_install)
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(libunwind)
BuildRequires: pkgconfig(libelf)
BuildRequires: cmake
BuildRequires: pkg-config
Source0:       %{name}-%{version}.tar.gz
ExclusiveArch: %{x86_64} %{arm64} %{arm32} %{ix86}'

%description
the bionic linker under bionic_translation/linker/ is taken from https://github.com/Cloudef/android2gnulinux and partly modified for our purposes
the pthread wrapper under bionic_translation/pthread_wrapper/ is taken from the same place, and augmented with additional missing wrapper functions
same with bionic_translation/libc/
bionic_translation/wrapper/ is a helper for these, also from android2gnulinux
bionic_translation/libstdc++_standalone is taken from bionic sources and coerced to compile; it's just "a minimum implementation of libc++ functionality not provided by compiler",
and things break when it's not linked in and android libs try to call into it and instead end up in the glibc or llvm libc++ implementations

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%exclude %{_libdir}/lib*.so
%{_libdir}/lib*.so.*
%{_datadir}/%{name}/cfg.d/%{name}.cfg
