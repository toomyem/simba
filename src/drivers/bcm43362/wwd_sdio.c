/**
 * @file wwd_sdio.c
 * @version 1.0.0
 *
 * @section License
 * Copyright (C) 2014-2016, Erik Moqvist
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * This file is part of the Simba project.
 */

#include "simba.h"

#include "network/wwd_buffer_interface.h"

wwd_result_t host_platform_sdio_transfer(wwd_bus_transfer_direction_t direction,
                                         sdio_command_t command,
                                         sdio_transfer_mode_t mode,
                                         sdio_block_size_t block_size,
                                         uint32_t argument,
                                         uint32_t* data,
                                         uint16_t data_size,
                                         sdio_response_needed_t response_expected,
                                         uint32_t* response)
{
    return (WWD_SUCCESS);
}

wwd_result_t host_platform_sdio_enumerate()
{
    return (WWD_SUCCESS);
}

void host_platform_enable_high_speed_sdio()
{
}

void sdio_irq()
{
}

wwd_result_t host_platform_unmask_sdio_interrupt()
{
    return (WWD_SUCCESS);
}

wwd_result_t host_enable_oob_interrupt()
{
    return (WWD_SUCCESS);
}

uint8_t host_platform_get_oob_interrupt_pin()
{
    return (0);
}