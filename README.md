odon
====

On-Demand ONions: utility to create Tor hidden services on-demand

Purpose
=======

At 31C3, there was discussion of possible censorship mechanisms for
Tor.  While the context was laudable (preventing Tor from becoming a
heaven for child pornography sites), I don't think a mechanism for
censorship should ever be built into Tor.

The proposed solution was to distribute a blacklist of .onion
addresses (or their hashes, or a bloom filter, or something similar)
to relays or clients, opt-in or opt-out. This tool exists as a quick
proof that such a mechanism wouldn't work, because blacklists can't
work in an environment where address creation is fast, cheap and
decentralized whereas maintaining the blacklist and distributing it is
a lot more expensive.

The basic idea is as follows:
* A hidden service can have N addresses for "advertising". These
  addresses are advertised to new users of the service via other
  channels,
* When an user visits an advertising address, they obtain a new
  address.  This address is generated on-the-fly to point to the
  actual content. It is never shown to another user, so the only
  person able to block it is the person who got it. It is impossible
  to exhaust all the addresses generated this way as it would require
  exhausting all possible .onion address space (2^80 addresses, about
  10^24).
* In case a user's address is blocked and they lose access to the
  advertising service, they may have the option to generate backup
  addresses that they can keep secret.

Status
======

This is just a quick experiment I came up with during the last hours of 31C3.
It is not used in production anywhere. But it is usable.

Development/running
===================

The Dockerfile provided lets you run a tor daemon and odon in a docker
container.

	$ docker build -t tor .
	$ docker run -p 9051 -p 5000 tor

To use odon from a browser, navigate to `http://localhost:5000/`.

Integrating with your tor service
=================================

You need to set up your own hidden service to start with. This service
will lead to a Python application handler, e.g. using flask. Look at
the provided code on how flask is integrated to generate hostnames on
demand.

Odon needs to have read access to the Tor config. On many systems this
means chmodding a lot of files, or running Odon as root (you probably
shouldn't do that). Adapting the existing docker-based solution may be
preferrable for your needs. Be aware, however, that Docker doesn't
provide a security barrier, and jobs running as root in a docker
container may escape the container.
