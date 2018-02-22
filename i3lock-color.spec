Name:           i3lock-color
Version:        c85ced646e1cd134f119732793b50e3fed8ac0c4
Release:        1%{?dist}
Summary:        This is just a re-patched version of i3lock with the commits from i3lock-color

License:        BSD
URL:            https://github.com/torvitas/i3lock-next.spec
Source0:        https://github.com/PandorasFox/i3lock-color/archive/c85ced646e1cd134f119732793b50e3fed8ac0c4.tar.gz

BuildRequires:  libxcb-devel
BuildRequires:  cairo-devel
BuildRequires:  libev-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  pam-devel
BuildRequires:  xcb-util-devel
BuildRequires:  autoconf
Requires:       libev
Requires:       libjpeg-turbo
Requires:       libxcb
Requires:       libxkbcommon
Requires:       libxkbcommon-x11
Requires:       pkg-config
Requires:       xcb-util-image

%global debug_package %{nil}

%description
i3lock is a simple screen locker like slock. After starting it, you will see a white screen (you can configure the color/an image). You can return to your screen by entering your password.

%prep
%autosetup

%build
autoreconf -i
./configure
%make_build prefix=/usr

%install
rm -rf %{buildroot}
%make_install prefix=/usr


%files
%license LICENSE
%doc README.md
%{_bindir}/i3lock
/usr/etc/pam.d/i3lock
/usr/share/man/man1/i3lock.1.gz

%changelog
* Wed Feb 21 2018 Sascha Marcel Schmidt <mail@saschaschmidt.net>
- Initial version of the package.
