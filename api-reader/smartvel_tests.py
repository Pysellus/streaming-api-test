from threading import Thread

from rx import Observable

from APIReaderSmartvel import APIReaderSmartvel

events = Observable.from_(APIReaderSmartvel().get_iterable())


# Verify that all the following regions have events
REGIONS = (
    'Barcelona',
    'Málaga',
    'Palma de Mallorca'
)

# Filters
def has_place(element):
    return 'place' in element['event']

is_in_region = { region: lambda element: element['event']['place']['region']['name'] == region for region in REGIONS }


# Test
def is_not_empty(a_stream):
    a_stream.is_empty().subscribe(fail_if_empty)

# Test helper (just a console reporter)
def fail_if_empty(empty):
    if empty:
        print('stream should not be empty!')
    else:
        print('good, stream is not empty')



# Launch the test
threads = [ Thread(target=is_not_empty, \
                   args=(events.filter(has_place).filter(is_in_region[region]), )) \
            for region in REGIONS ]

for thread in threads:
    thread.start()

