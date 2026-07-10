%global tl_name breakurl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.40
Release:	%{tl_revision}.1
Summary:	Line-breakable \url-like links in hyperref when compiling via dvips/ps2pdf
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/breakurl
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/breakurl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/breakurl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/breakurl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a command much like hyperref's \url that typesets
a URL using a typewriter-like font. However, if the dvips driver is
being used, the original \url doesn't allow line breaks in the middle of
the created link: the link comes in one atomic piece. This package
allows such line breaks in the generated links.

