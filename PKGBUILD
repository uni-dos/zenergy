# Maintainer: bouhaa <boukehaarsma23 at gmail dot com>

_pkgname=zenergy
pkgname=$_pkgname-dkms-git
pkgver=11.91c3ca6
pkgrel=1
pkgdesc='Linux kernel driver for reading RAPL registers for AMD Zen CPUs'
arch=('x86_64' 'i686')
url='https://github.com/boukehaarsma23/zenergy'
license=('GPL2')
depends=('dkms')
provides=('zenergy-dkms')

source=("$_pkgname::git+$url.git"
        "dkms.conf")

b2sums=("SKIP"
       "5b574c8243405a10a8dc008874de865fbb89563d55f55c7549e4fb6174d1240d2aaafa344e7d18cffa5f6b5bbbaed88818601d05c892cf2a2589bc1507a308a2")

pkgver() {
  cd "$srcdir/$_pkgname"
  printf "%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  install -Dm644 "$srcdir/$_pkgname/dkms.conf" "$pkgdir/usr/src/$_pkgname-$pkgver/dkms.conf"
  install -Dm644 "$srcdir/$_pkgname/Makefile" "$pkgdir/usr/src/$_pkgname-$pkgver/Makefile"
  install -Dm644 "$srcdir/$_pkgname/zenergy.c" "$pkgdir/usr/src/$_pkgname-$pkgver/zenergy.c"
}
