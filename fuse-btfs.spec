Summary:	FUSE filesystem Bittorrent
Name:		fuse-btfs
Version:	2.8
Release:	1%{?dist}

Group:		System Environment/Base
License:	GPLv3
URL:		https://github.com/johang/btfs
Source0:	btfs-%{version}.tar.gz

BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(libtorrent-rasterbar)
BuildRequires:	pkgconfig(libcurl)


%description
With BTFS, you can mount any .torrent file or magnet link and then use it as
any read-only directory in your file tree. The contents of the files will be
downloaded on-demand as they are read by applications. Tools like ls, cat and
cp works as expected. Applications like vlc and mplayer can also work without
changes.

%prep
%setup -q -n btfs-%{version}

%build
autoreconf -i
%configure
make %{?_smp_mflags}

%install
%{make_install}

%files
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Mar  1 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 2.8-1.R
- initial build
